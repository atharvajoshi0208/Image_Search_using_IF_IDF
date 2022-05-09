from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from  wtforms.validators import DataRequired



class SerachForm(FlaskForm):
    Search = StringField(label = 'Search query',id='SearchQuery',validators=[DataRequired()])
    Submit = SubmitField(label='Search')