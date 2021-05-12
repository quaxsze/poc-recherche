from flask import Flask
from flask_cors import CORS
from elasticsearch import Elasticsearch

from backend.utils import download_baserow_api
from backend.config import Config


def create_app() -> Flask:
    app: Flask = Flask(__name__,
                       static_folder="../dist/static",
                       template_folder="../dist")

    # CORS only for local dev
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

    app.config.from_object(Config)

    app.elasticsearch = Elasticsearch(
        [app.config["ELASTICSEARCH_URL"]]) if app.config["ELASTICSEARCH_URL"] else None

    result_list: list = download_baserow_api(
        app.config["BASEROW_ORG_BADGES_TO_BOOST_URL"])
    app.config['ORG_BADGES_TO_BOOST'] = []
    for result in result_list:
        if result['field_98434']:
            app.config['ORG_BADGES_TO_BOOST'].append(result['field_98433'])

    # register the database command
    from backend import db
    db.init_app(app)

    from backend import routes
    app.register_blueprint(routes.bp)

    return app
