from werkzeug.wrappers import Response
from elasticsearch import client
from flask import render_template, jsonify, request, current_app, Blueprint

bp = Blueprint("api", __name__)


@bp.route("/api", methods=["POST"])
def api() -> Response:
    query_text: str = request.json['search_text']
    title_boost: int = request.json['boost_dataset_title']
    description_boost: int = request.json['boost_dataset_description']
    org_title_boost: int = request.json['boost_org_title']
    weight_dataset_featured: int = request.json['weight_dataset_featured']
    weight_org_public_service: int = request.json['weight_org_public_service']
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
                        "weight": weight_org_public_service
                    },
                    {
                        "filter": {
                            "terms": {
                                "organization_badges.keyword": current_app.config['ORG_BADGES_TO_BOOST']
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


@bp.route("/api/<dataset_remote_id>", methods=["GET"])
def get_dataset(dataset_remote_id: str) -> Response:
    es: client.Elasticsearch = current_app.elasticsearch

    query_body: dict = {
        "query": {
            "term": {
                "remote_id": {
                    "value": dataset_remote_id
                }
            }
        }
    }
    result: dict = es.search(index='datasets', body=query_body, explain=True)
    return jsonify({
        "dataset": result['hits']['hits'][0]['_source']
    })


@bp.route("/", defaults={"path": ""})
# allows routing in vuejs
@bp.route("/<path:path>")
def index(path: str) -> Response:
    return render_template("index.html")
