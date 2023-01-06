from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import declarative_base

from config import db

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nulladle=False)
    login = Column(String(120), nulladle=False, unique=True)
    password = Column(String(30), nulladle=False)
    email = Column(String(120), nulladle=False, unique=True)
    date_create = Column(DateTime, default=datetime.utcnow)
    date_update = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)


class CategoryElf(db.Model):
    __tablename__ = 'category_elfs'

    id = Column(Integer, primary_key=True, nulladle=False)
    name = Column(String(120), nulladle=False)
    is_active = Column(Boolean, default=True)
    date_create = Column(DateTime, default=datetime.utcnow)


class Elf(db.Model):
    __tablename__ = 'elfs'

    id = Column(Integer, primary_key=True, nulladle=False)
    name = Column(String(120), nulladle=False)
    patronymic = Column(String(120))
    last_name = Column(String(120), nulladle=False)
    nickname = Column(String(120))
    photo = Column(String(120), nulladle=False)
    category_elf = Column(ForeignKey(CategoryElf.id))
    quote = Column(Text, nulladle=False)
    date_quote = Column(DateTime)
    date_create = Column(DateTime, default=datetime.utcnow)
    date_update = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    moderator = Column(ForeignKey(User.id))
