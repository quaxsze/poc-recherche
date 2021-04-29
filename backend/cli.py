import csv
from urllib.request import urlopen
from tempfile import NamedTemporaryFile, _TemporaryFileWrapper

import click
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from config import Config


DATASET_CATALOG_URL = 'https://www.data.gouv.fr/fr/datasets/r/f868cca6-8da1-4369-a78d-47463f19a9a3'
ORG_CATALOG_URL = 'https://www.data.gouv.fr/fr/datasets/r/b7bbfedc-2448-4135-a6c7-104548d396e7'


@click.group()
def cli():
    pass


def download_catalog(url: str, fd: _TemporaryFileWrapper) -> None:
    response = urlopen(url)
    while True:
        chunk = response.read(1024)
        if not chunk:
            break
        fd.write(chunk)


@cli.command()
def init_db() -> None:
    es = Elasticsearch([Config.ELASTICSEARCH_URL])

    click.echo("Initializing the database.")
    try:
        es.indices.delete(index='datasets')
    except NotFoundError:
        pass

    with NamedTemporaryFile(delete=False) as dataset_fd:
        download_catalog(DATASET_CATALOG_URL, dataset_fd)
    with NamedTemporaryFile(delete=False) as org_fd:
        download_catalog(ORG_CATALOG_URL, org_fd)

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
                            'organization_badges': org['badges']
                        })
                es.index(index='datasets', id=counter, body=body)
                counter += 1
    click.echo("Done.")


if __name__ == "__main__":
    cli()
