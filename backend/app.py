from werkzeug.wrappers import Response
from elasticsearch import Elasticsearch, client
from flask import Flask, render_template, jsonify, request, current_app
from flask_cors import CORS
from .config import Config


app: Flask = Flask(__name__,
            static_folder="../dist/static",
            template_folder="../dist")
# CORS only for local dev
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

app.config.from_object(Config)
app.elasticsearch = Elasticsearch([app.config["ELASTICSEARCH_URL"]]) \
    if app.config["ELASTICSEARCH_URL"] else None


@app.route("/api", methods=["POST"])
def api() -> Response:
    query_text: str = request.json['search_text']
    title_boost: int = request.json['boost_dataset_title']
    description_boost: int = request.json['boost_dataset_description']
    org_title_boost: int = request.json['boost_org_title']
    weight_dataset_featured: int = request.json['weight_dataset_featured']
    weight_org_badge: int = request.json['weight_org_badge']

    fields: list = [
        f'title^{title_boost}',
        f'description^{description_boost}',
        f'organization_name^{org_title_boost}',
        ]

    es: client.Elasticsearch = current_app.elasticsearch

    query_body: dict = {
        "query": {
            "function_score": {
                "query": {
                    "multi_match": {
                        "query": query_text,
                        "fields": fields
                    }
                },
                "functions": [
                    {
                        "filter": {
                            "match": {
                                "featured": "true"
                            }
                        },
                        "weight": weight_dataset_featured
                    },
                    {
                        "filter": {
                            "match": {
                                "organization_badges": "public-service"
                            }
                        },
                        "weight": weight_org_badge
                    }
                ],
                "score_mode": "multiply",
                "boost_mode": "multiply"
            }
        }
    }
    result: dict = es.search(index='datasets', body=query_body, explain=True)

    results_number: int = result['hits']['total']['value']
    res: list = []
    for hit in result['hits']['hits']:
        res.append({
            'source': hit['_source'],
            'explain': hit['_explanation']
        })
    return jsonify({
        "results_number": results_number,
        "results": res
    })


@app.route("/", defaults={"path": ""})
# allows routing in vuejs
@app.route("/<path:path>")
def index(path: str) -> Response:
    return render_template("index.html")
