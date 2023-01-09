#!/usr/bin/env python3
from models import db
from config import app

with app.app_context():
    db.create_all()
