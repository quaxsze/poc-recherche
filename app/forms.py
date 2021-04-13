from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField('Recherche', validators=[
                         DataRequired()], render_kw={'placeholder': 'Rechercher'})
    boost_value = IntegerField('Boost de', default=1)
    boost_select = SelectField(
        'Sur', choices=[('title', 'Titre'), ('description', 'Description'), ('organization', 'Organisation')])
    submit = SubmitField('Valider')
