from flask import render_template, redirect, url_for, abort
# importing main from main blueprint
from . import main
# importing database
from .. import db, photos
# b blog impot forms
from .forms import BlogForm, SubscribeForm, CommentForm
# decorator that will user authentication
from flask_login import login_required, current_user
# importing wft
from flask_wtf import FlaskForm
# importing class models
from ..models import Blog, Subscribe, Comment


@main.route('/')
def index():
    title = 'Home is best'
    subscribe = SubscribeForm()

    if subscribe.validate_on_submit():
        email = subscribe.title.data

        new_sub = Subscribe(email=email)

        new_sub.save_blog()

    return render_template('index.html', title=title, subscribe=subscribe)


@main.route('/blog', methods=['GET', 'POST'])
def blog():
    blogForm = BlogForm()
    title = 'The blog'

    if blogForm.validate_on_submit():
        title = blogForm.title.data
        blog = blogForm.blog.data
        date = blogForm.date.data
        pic_url = blogForm.data

        new_blog = Blog(title=title, blog=blog,
                        posted=date, blog_pic_path=pic_url)
        new_blog.save_blog()

    blogs = Blog.get_blogs()
    return render_template('blog.html', title=title, blogs=blogs, blogForm=blogForm)


@main.route('/blog/<int:id>', methods=['GET', 'POST'])
def comment(id):
    commentForm = CommentForm()
    title = 'The blog'

    if commentForm.validate_on_submit():
        comment = commentForm.comment.data
        tag = commentForm.tagger.data

        new_comment = Comment(comment=comment, tagger=tag, blog_id=id)
        new_comment.save_comment()

    comments = Comment.get_comments(id)

    blogs = Blog.get_blogs()
    return render_template('blog.html', title=title, blogs=blogs, blogForm=blogForm, comments=comments)
