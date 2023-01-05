from datetime import datetime

from config import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nulladle=False)
    login = db.Column(db.String(120), nulladle=False, unique=True)
    password = db.Column(db.String(30), nulladle=False)
    email = db.Column(db.String(120), nulladle=False, unique=True)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)
    date_update = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
