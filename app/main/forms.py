from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required

class BlogForm(FlaskForm):
    '''
    Blog adding
    '''
    title