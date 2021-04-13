import os

class Config(object):
    SECRET_KEY = 'you-will-never-guess'
    ELASTICSEARCH_URL = os.environ['ELASTICSEARCH_URL']
