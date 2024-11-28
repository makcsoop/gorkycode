import sqlalchemy
from sqlalchemy import orm
import datetime
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    role = sqlalchemy.Column(sqlalchemy.Integer)


class Newsfeed(SqlAlchemyBase):
    __tablename__ = 'newsfeed'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_user = sqlalchemy.Column(sqlalchemy.Integer)
    image = sqlalchemy.Column(sqlalchemy.String)
    text = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.DateTime)
    like = sqlalchemy.Column(sqlalchemy.Integer)


class Dialog(SqlAlchemyBase):
    __tablename__ = 'dialog'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_users = sqlalchemy.Column(sqlalchemy.String)

class Message(SqlAlchemyBase):
    __tablename__ = 'message'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_dialog = sqlalchemy.Column(sqlalchemy.Integer)
    id_user = sqlalchemy.Column(sqlalchemy.Integer)
    text = sqlalchemy.Column(sqlalchemy.String)
    data = sqlalchemy.Column(sqlalchemy.DateTime)


class Settings(SqlAlchemyBase):
    __tablename__ = 'settings'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_user = sqlalchemy.Column(sqlalchemy.Integer)
    theme = sqlalchemy.Column(sqlalchemy.Integer)
    vision = sqlalchemy.Column(sqlalchemy.Integer)






