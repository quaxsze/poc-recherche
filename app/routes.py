from flask import Blueprint, render_template, current_app
from app.forms import SearchForm

bp = Blueprint('main', __name__)

FIELDS = ['title', 'description', 'organization']

@bp.route('/', endpoint='index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        query: str = form.search.data
        boost_value: int = form.boost_value.data
        boost_select: str = form.boost_select.data
        fields: list = []

        for field in FIELDS:
            if field == boost_select:
                fields.append(f'{field}^{boost_value}')
            else:
                fields.append(field)

        es = current_app.elasticsearch
        result = es.search(index='datasets', body={'query': {'multi_match': {
                           'query': query, 'fields': fields}}}, explain=True)

        results_number: int = result['hits']['total']['value']
        res: list = []
        for hit in result['hits']['hits']:
            res.append({
                'source': hit['_source'],
                'explain': hit['_explanation']
            })
        return render_template('index.html', form=form, search_results=res, results_number=results_number)
    return render_template('index.html', form=form)
