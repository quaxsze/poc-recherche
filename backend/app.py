from elasticsearch import Elasticsearch
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
def api():
    query_text: str = request.json['search_text']
    title_boost: str = request.json['boost_dataset_title']
    description_boost: str = request.json['boost_dataset_description']
    org_title_boost: str = request.json['boost_org_title']
    fields: list = [
        f'title^{title_boost}',
        f'description^{description_boost}',
        f'organization_name^{org_title_boost}',
        ]

    es = current_app.elasticsearch

    query_body = {
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
                        "weight": 10
                    },
                    {
                        "filter": {
                            "match": {
                                "organization_badges": "public-service"
                            }
                        },
                        "weight": 2
                    }
                ],
                "score_mode": "multiply",
                "boost": "5",
                "boost_mode": "multiply"
            }
        }
    }
    result = es.search(index='datasets', body=query_body, explain=True)

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
def index(path: str):
    return render_template("index.html")
