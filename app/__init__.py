# import flask
from flask import Flask

# for styling css
from flask_bootstrap import Bootstrap

# import config options form config
from config import config_options

# SQl toolkit for python
from flask_sqlalchemy import SQLAlchemy

# flask login add
from flask_login import LoginManager


# from flask_uploads import UploadSet, configure_uploads, IMAGES


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()

# assign SQLAlcehmy to db
db = SQLAlchemy()
# photos = UploadSet('photos', IMAGES)


def create_app(config_name):

    # intiating flask us a app
    app = Flask(__name__)

    # getting bootstrap form app
    bootstrap.init_app(app)

    # Initializing flask extensions
    db.init_app(app)

    # allows to get settings form config
    app.config.from_object(config_options[config_name])

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # login manager
    login_manager.init_app(app)

    # blueprint of the authnication
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    # configure UploadSet
    # configure_uploads(app, photos)

    return app
