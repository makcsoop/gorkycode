from flask import Flask, request, session
from scripts import *
import sqlalchemy
import requests
from flask_login import LoginManager, login_user
from data import db_session
from data.users import User, Dialog, Message, Settings, Newsfeed
from data.db_session import global_init, SqlAlchemyBase

# яндекс ключ к картам  f9727fb1-f338-4780-b4c4-d639d0a62107
#http://localhost:8000/registration?login=user1&name=max&password=1234&password2=12&email=max@gmail.com

#http://localhost:8000/authorization?login=user&password=1234

test = {"login": "user", "password" : "1234", "password2": "1234", "name": "", "email":""}
ENTRANCE = False
ID = -1
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

db_session.global_init('db/base.db')

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

db_sess = db_session.create_session()

@app.route('/authorization', methods=['GET'])
def login():
    session['login'] = ''
    session['role'] = 0
    session['id'] = -1
    args = request.args
    login = args.get('login')
    password = args.get('password')
    #db_sess = db_session.create_session()
    login_cur = db_sess.query(User).filter(User.login == str(login)).first()
    if len(login) and len(password):
        login_cur = db_sess.query(User).filter(User.login == login, User.password == password).first()
        if login_cur:
            ID = get_id(login)
            session['id'] = ID
            session['login'] = login
            print(login_cur)
            # session['role'] = get_level_user(login)
            return {"flag": 1}
        else:
            return {"flag": 2}
    else:
        return {"flag": 0}
    
    
@app.route("/registration", methods=['GET'])
def registration():
    args = request.args
    login = args.get('login')
    name = args.get('name')
    email = args.get('email')
    password = args.get('password')
    #db_sess = db_session.create_session()
    if not (isvalid_login(login)):
        return {"flag": 0}
    if  isvalid_value(login, password, name):
        login_cur = db_sess.query(User).filter(User.login == login).first()
        if login_cur:
            print(login_cur)
            return {"flag": 0}
        user = User()
        user.name = name
        user.login = login
        user.email = email
        user.password = password
        user.role = 1
        db_sess.add(user)
        db_sess.commit()
        return {"flag": 1}
    else:
        return {"flag": 3} #не все поля заполнины
    

@app.route("/map", methods=['GET'])
def map():
    pass

@app.route("/newsfeed", methods=['GET'])
def newsfeed():
    # НУЖНО ВЫБРАТЬ КАК ВЫДАВАТЬ ПОСТЫ ЛИБО ПО ПОДПИСКАМ ЛИБО ВСЕ ПУБЛИКАЦИИ ЧЕЛОВ
    ID = session.get("id")
    if ID != -1:
        login_cur = db_sess.query(Newsfeed).filter(Newsfeed.id_user == ID)
        final = []
        for i in login_cur:
            info_user = db_sess.query(User).filter(User.id == id)

        
    else:
        return {"flag": 0}

@app.route("/messenger", methods=['GET'])
def messenger():
    ID = session.get("id")
    if ID != -1:
        #http://localhost:8000/messenger
        search = "%{}%".format(ID)
        #db_sess = db_session.create_session()
        login_cur = db_sess.query(Dialog).filter(Dialog.id_users.like(search))
        return {"flag": 1, "dialog": [str(i.id_users) for i in login_cur], "search": search, "ID" : ID}
    else:
        return {"flag": 0}

@app.route("/correspondence", methods=['GET'])
def correspondence():
    #http://localhost:8000/correspondence?dialog=1
    ID = session.get("id")
    if ID != -1:
        args = request.args
        id_dialog = args.get('dialog')
        #db_sess = db_session.create_session()
        login_cur = db_sess.query(Message).filter(Message.id_dialog == id_dialog)
        final = [[1 if i.id_user == ID else 0, i.text, i.date] for i in login_cur]
        final = sorted(final, key=lambda x: x[2])
        return {"flag": 1, "info": final}

    else:
        return {"flag": ID}

@app.route("/other", methods=['GET'])
def other():
    if ID != -1:
         pass
    else:
        return {"flag": 0}

@app.route("/profile", methods=['GET'])
def profile():
    ID = session.get("id")
    if ID != -1:
        #db_sess = db_session.create_session()
        login_cur = db_sess.query(User).filter(User.id == ID).first()
        return {"flag": 1, "name": login_cur.name, "login": login_cur.login, "email": login_cur.email} 
    else:
        return {"flag": 0}

@app.route("/friends", methods=['GET'])
def friends():
    if ID != -1:
        pass
    else:
        return {"flag": 0}

@app.route("/communities",methods=['POST', 'GET'])
def communities():
    if ID != -1:
        pass
    else:
        return {"flag": 0}

@app.route("/settings", methods=['GET'])
def settings():
    ID = session.get("id")
    if request.method == 'POST' and ID != -1:
        pass
        #передать тему и просто поменять значение в базе
    else:
        if ID != -1:
            login_cur = db_sess.query(Settings).filter(Settings.id_user == ID).first()
            return {"flag": 1, "theme": login_cur.theme}
        else:
            return {"flag": 0}
    

if __name__ == '__main__':
    app.run(port=8000, host='localhost')
