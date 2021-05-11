import os
from flask import Flask, session, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from functools import wraps
from flask_login import LoginManager

db = SQLAlchemy()
DB_DATABASE= "video.db"

def create_up():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dfccvvdssdfbccvdffewgeher bfdfsfggdgfgefgfbbdss'
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_DATABASE}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    from .views import views
    from .homepage import homepage

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(homepage, url_prefix='/')

    from .database import User, Video
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'homepage.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("website/" + DB_DATABASE):
        db.create_all(app=app)
        print("ok!")




