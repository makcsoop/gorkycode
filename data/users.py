import sqlalchemy
from sqlalchemy import orm
import datetime
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String)
    id_image = sqlalchemy.Column(sqlalchemy.Integer)
    password = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    role = sqlalchemy.Column(sqlalchemy.Integer)
    activity = sqlalchemy.Column(sqlalchemy.Integer)


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

class Friends(SqlAlchemyBase):
    __tablename__ = 'friends'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_users = sqlalchemy.Column(sqlalchemy.Integer)


class Communities(SqlAlchemyBase):
    __tablename__ = 'communities'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_image = sqlalchemy.Column(sqlalchemy.Integer)
    name = sqlalchemy.Column(sqlalchemy.String)
    activity = sqlalchemy.Column(sqlalchemy.Integer)

    
class Feedcommunities(SqlAlchemyBase):
    __tablename__ = 'feedcommunities'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_communities = sqlalchemy.Column(sqlalchemy.String)
    id_image = sqlalchemy.Column(sqlalchemy.String)
    # url = sqlalchemy.Column(sqlalchemy.String)
    text = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.DateTime)
    like = sqlalchemy.Column(sqlalchemy.Integer)
    x = sqlalchemy.Column(sqlalchemy.Integer)
    y = sqlalchemy.Column(sqlalchemy.Integer)
    address = sqlalchemy.Column(sqlalchemy.String)



class ProblemPoints(SqlAlchemyBase):
    __tablename__ = 'problempoints'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    x = sqlalchemy.Column(sqlalchemy.Integer)
    y = sqlalchemy.Column(sqlalchemy.Integer)
    description = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)


class Parking(SqlAlchemyBase):
    __tablename__ = 'parking'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    x = sqlalchemy.Column(sqlalchemy.Integer)
    y = sqlalchemy.Column(sqlalchemy.Integer)
    description = sqlalchemy.Column(sqlalchemy.String)



class Role(SqlAlchemyBase):
    __tablename__ = 'role'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    level = sqlalchemy.Column(sqlalchemy.Integer)


class Image(SqlAlchemyBase):
    __tablename__ = 'image'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    url = sqlalchemy.Column(sqlalchemy.String)
    

class Wait_Communities(SqlAlchemyBase):
    __tablename__ = 'waitcommunities'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_user = sqlalchemy.Column(sqlalchemy.Integer)
    name = sqlalchemy.Column(sqlalchemy.String)
    target = sqlalchemy.Column(sqlalchemy.String)
    image = sqlalchemy.Column(sqlalchemy.String)
    activity = sqlalchemy.Column(sqlalchemy.Integer)


class Logging(SqlAlchemyBase):
    __tablename__ = 'logging'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_log = sqlalchemy.Column(sqlalchemy.Integer)
    data = sqlalchemy.Column(sqlalchemy.DateTime)
    notes = sqlalchemy.Column(sqlalchemy.String)


class TypeLog(SqlAlchemyBase):
    __tablename__ = 'typelog'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    type = sqlalchemy.Column(sqlalchemy.String)


class ParkZone(SqlAlchemyBase):
    __tablename__ = 'parkzone'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_pair = sqlalchemy.Column(sqlalchemy.Integer)
    x = sqlalchemy.Column(sqlalchemy.Integer)
    y = sqlalchemy.Column(sqlalchemy.Integer)
    description = sqlalchemy.Column(sqlalchemy.String)

    
    









