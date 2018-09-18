from . import db
from flask_login import UserMixin

from datetime import datetime


# used for password hashing
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager


class User(UserMixin, db.Model):
    '''
    user class model with username, passwords
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship('Blog', backref='users', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Blog(db.Model):
    '''
    Blog user post
    '''
    __tablename = 'blog'

    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer)
    title = db.Column(db.String(140))
    blog = db.Column(db.String())
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    # blog_pic_path = (db.String(255))
    # end of true feilds
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship('Comment', backref='blog', lazy='dynamic')

    def save_blog(self):
        '''
        save blog
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls):
        '''
        get blog from db
        '''
        bloges = Blog.query.order_by('-id').all()

        return bloges

    @classmethod
    def get_blog(cls, id):
        '''
        get a blog
        '''
        blog = Blog.query.filter_by(id=id).first()

        return blog


class Comment(db.Model):
    '''
    Comment model containing user comments
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    tagger = db.Column(db.String(255))
    # foreign key
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        '''
        get comments by comments id
        '''
        comments = Comment.query.filter_by(blog_id=id).all()

        return comments

    @classmethod
    def get_comment(cls, id):
        '''
        gets a single comment
        '''
        comment = Comment.query.filter_by(id=id).first()
        return comment


class Subscribe(db.Model):
    '''
    model for the class subscribe
    '''
    __tablename__ = 'subscribe'

    id = db.Column(db.Integer, primary_key=True)
    tagger = db.Column(db.String(255))
    email = db.Column(db.String(255))
