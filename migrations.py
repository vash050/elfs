#!/usr/bin/env python
from models import db
from config import app

with app.app_context():
    db.create_all()
