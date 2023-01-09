from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text

from config import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elfs.db'
db = SQLAlchemy(app)


# TODO нет таблицы в базе
class UserSite(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(120), nullable=False)
    login = Column(String(120), nullable=False)
    password = Column(String(30), nullable=False)
    email = Column(String(120), nullable=False)
    date_create = Column(DateTime, default=datetime.now)
    date_update = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=True)


class CategoryElf(db.Model):
    __tablename__ = 'category_elfs'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(120), nullable=False)
    is_active = Column(Boolean, default=True)
    date_create = Column(DateTime, default=datetime.now)


class Elf(db.Model):
    __tablename__ = 'elfs'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(120), nullable=False)
    patronymic = Column(String(120))
    last_name = Column(String(120), nullable=False)
    nickname = Column(String(120))
    photo = Column(String(120))
    category_elf = Column(ForeignKey(CategoryElf.id))
    quote = Column(Text, nullable=False)
    date_quote = Column(String(120))
    date_create = Column(DateTime, default=datetime.now)
    date_update = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=True)
    moderator = Column(ForeignKey(UserSite.id))
