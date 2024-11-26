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
    






