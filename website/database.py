from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)
    videos = db.relationship('Video')

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    link = db.Column(db.String(50))
    description = db.Column(db.String(300))
    uploaded_time = db.Column(db.DateTime(timezone=True), default=datetime.now())
    modified_time = db.Column(db.DateTime(timezone=True), default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))