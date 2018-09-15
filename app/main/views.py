from flask import render_template, redirect, url_for, abort

# importing main from main blueprint
from . import main

# importing database
# from .. import db



# decorator that will user authentication
from flask_login import login_required, current_user

# importing wft
from flask_wtf import FlaskForm


@main.route('/')
def index():
    title = 'Home is best'
   
    return render_template('index.html', title=title)
