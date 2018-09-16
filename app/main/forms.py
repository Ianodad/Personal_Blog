from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField

from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required


class BlogForm(FlaskForm):
    '''
    Blog adding
    '''
    title = StringField('Your title here', validators=[Required()])
    blog = TextAreaField('Your Post here', validators=[Required()])
    pic_url = StringField('Photo URL', validators=[Required()], render_kw={
                          'placeholder': 'Photo URL'})
    date = DateField('Post Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')
