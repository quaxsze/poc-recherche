import ast
import csv
from tempfile import NamedTemporaryFile

import click
from flask import current_app
from flask.cli import with_appcontext
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from backend.utils import download_catalog, download_baserow_api


def init_db():
    es = Elasticsearch([current_app.config['ELASTICSEARCH_URL']])

    try:
        es.indices.delete(index='datasets')
        click.echo("Deleted the previous index.")
    except NotFoundError:
        pass

    with NamedTemporaryFile(delete=False) as dataset_fd:
        download_catalog(current_app.config['DATASET_CATALOG_URL'], dataset_fd)
    with NamedTemporaryFile(delete=False) as org_fd:
        download_catalog(current_app.config['ORG_CATALOG_URL'], org_fd)

    results_list: list = download_baserow_api(
        current_app.config['BASEROW_ORG_TYPOLOGY_URL'])

    with open(dataset_fd.name) as dataset_csvfile, open(org_fd.name) as org_csvfile:
        dataset_rows = list(csv.DictReader(dataset_csvfile, delimiter=';'))
        org_rows = list(csv.DictReader(org_csvfile, delimiter=';'))
        with click.progressbar(dataset_rows) as bar:
            counter = 1
            for dataset in bar:
                body = {
                    'remote_id': dataset['id'],
                    'title': dataset['title'],
                    'url': dataset['url'],
                    'description': dataset['description'],
                    'featured': dataset['featured']
                }
                for org in org_rows:
                    if org['id'] == dataset['organization_id']:
                        body.update({
                            'organization_name': org['name'],
                            'organization_badges': ast.literal_eval(org['badges'])
                        })
                        for result in results_list:
                            if result['field_98460'] == org['id']:
                                for item in ast.literal_eval(result['field_98464']):
                                    body['organization_badges'].append(item)

                es.index(index='datasets', id=counter, body=body)
                counter += 1


@click.command("init-db")
@with_appcontext
def init_db_command():
    click.echo("Initializing the database.")
    init_db()
    click.echo("Done.")


def init_app(app):
    app.cli.add_command(init_db_command)
