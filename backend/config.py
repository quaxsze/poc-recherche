import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ELASTICSEARCH_ADDR = os.environ.get(
        'DOKKU_ELASTICSEARCH_POC_RECHERCHE_INDEX_PORT_9200_TCP_ADDR') or 'localhost'
    ELASTICSEARCH_PORT = os.environ.get(
        'DOKKU_ELASTICSEARCH_POC_RECHERCHE_INDEX_PORT_9200_TCP_PORT') or '9200'
    ELASTICSEARCH_URL = f'http://{ELASTICSEARCH_ADDR}:{ELASTICSEARCH_PORT}'
    BASEROW_API_TOKEN = 'secret-secret'
    BASEROW_ORG_TYPOLOGY_URL = 'https://api.baserow.io/api/database/rows/table/18703/'
    BASEROW_ORG_BADGES_TO_BOOST_URL = 'https://api.baserow.io/api/database/rows/table/18698/'
    DATASET_CATALOG_URL = 'https://www.data.gouv.fr/fr/datasets/r/f868cca6-8da1-4369-a78d-47463f19a9a3'
    ORG_CATALOG_URL = 'https://www.data.gouv.fr/fr/datasets/r/b7bbfedc-2448-4135-a6c7-104548d396e7'
