from elasticsearch import Elasticsearch
from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)

    import os
    os.environ['ELASTICSEARCH_URL']

    app.config.from_object(config_class)
    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    from app import db
    db.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    return app
