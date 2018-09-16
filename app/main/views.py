from flask import render_template, redirect, url_for, abort
# importing main from main blueprint
from . import main
# importing database
from .. import db
# b blog impot forms
from .forms import BlogForm
# decorator that will user authentication
from flask_login import login_required, current_user
# importing wft
from flask_wtf import FlaskForm
# importing class models
from ..models import Blog


@main.route('/')
def index():
    title = 'Home is best'

    return render_template('index.html', title=title)


@main.route('/blog', methods=['GET', 'POST'])
def blog():
    blogForm = BlogForm()
    title = 'The blog'

    if blogForm.validate_on_submit():
        title = blogForm.title.data
        blog = blogForm.blog.data
        date = blogForm.date.data

        new_blog = Blog(title=title, blog=blog, posted=date)
        new_blog.save_blog()

    blogs = Blog.get_blogs()
    return render_template('blog.html', title=title, blogs=blogs, blogForm=blogForm)
