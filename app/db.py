import csv
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

import click
from flask import current_app
from flask.cli import with_appcontext


CATALOG_URL = 'https://www.data.gouv.fr/fr/datasets/r/f868cca6-8da1-4369-a78d-47463f19a9a3'


def download_catalog(url, fd):
    response = urlopen(url)
    # CHUNK = 16 * 1024
    while True:
        chunk = response.read(1024)
        if not chunk:
            break
        fd.write(chunk)


def init_db(url=CATALOG_URL):
    es = current_app.elasticsearch

    # es.indices.delete(index='datasets')

    with NamedTemporaryFile(delete=False) as fd:
        download_catalog(url, fd)
    with open(fd.name) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        rows = list(reader)
        with click.progressbar(rows) as bar:
            counter = 1
            for row in bar:
                es.index(index='datasets', id=counter, body={
                    'remote_id': row['id'],
                    'title': row['title'],
                    'url': row['url'],
                    'description': row['description'],
                    'organization': row['organization']
                })
                counter += 1


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.cli.add_command(init_db_command)
