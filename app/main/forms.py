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


class SubscribeForm(FlaskForm):
    '''
    Subscription form 
    '''
    email = TextAreaField('BECOME A FOLLOWER', validators=[Required()])
    submit = SubmitField('SUBSCRIBE!')


class CommentForm(FlaskForm):
    '''
    Comment form
    '''
    comment = TextAreaField('Comment of blog', validators=[Required()])
    tagger = StringField('Your gamer tag', validators=[Required()])
    submit = SubmitField('Comment')
