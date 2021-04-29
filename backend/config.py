import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ELASTICSEARCH_ADDR = os.environ.get(
        'DOKKU_ELASTICSEARCH_POC_RECHERCHE_INDEX_PORT_9200_TCP_ADDR') or 'localhost'
    ELASTICSEARCH_PORT = os.environ.get(
        'DOKKU_ELASTICSEARCH_POC_RECHERCHE_INDEX_PORT_9200_TCP_PORT') or '9200'
    ELASTICSEARCH_URL = f'http://{ELASTICSEARCH_ADDR}:{ELASTICSEARCH_PORT}'
