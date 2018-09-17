from flask import render_template, redirect, url_for, abort, flash
# importing main from main blueprint
from . import main
# importing database
from .. import db, photos
# importing database
from .. import db
# b blog impot forms
from .forms import BlogForm, SubscribeForm, CommentForm
# decorator that will user authentication
from flask_login import login_required, current_user
# importing wft
from flask_wtf import FlaskForm
# importing class models
from ..models import Blog, Subscribe, Comment

from flask_login import login_required


@main.route('/')
def index():
    title = 'Home is best'
    subscribe = SubscribeForm()

    if subscribe.validate_on_submit():
        email = subscribe.title.data

        new_sub = Subscribe(email=email)

        new_sub.save_blog()

    blogs = Blog.get_blogs()
    return render_template('index.html', title=title, subscribe=subscribe, blogs=blogs,)


@main.route('/blog', methods=['GET', 'POST'])
@login_required
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

        return redirect(url_for('main.index', id=id))

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

    blog = Blog.get_blog(id)
    return render_template('viewblog.html', blog=blog, commentForm=commentForm, comments=comments)


@main.route('/comment/delete/<int:id>')
@login_required
def delete_comment(id):
    '''
    delete comment
    '''
    comment = Comment.get_comment(id)

    db.session.delete(comment)
    db.session.commit()

    flash('Blog has been deleted')

    return redirect(url_for('main.index', id=id))


@main.route('/blog/delete/<int:id>')
@login_required
def delete_blog(id):
    '''
    delete blog
    '''
    blog = Blog.get_blog(id)

    db.session.delete(blog)
    db.session.commit()

    flash('Comment has been deleted')

    return redirect(url_for('main.index', id=id))
