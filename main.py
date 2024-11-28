from flask import Flask, request, session
from scripts import *
import sqlalchemy
import requests
from flask_login import LoginManager, login_user
from data import db_session
from data.users import User, Dialog, Message, Settings, Newsfeed, Friends, Communities, Feedcommunities
from data.db_session import global_init, SqlAlchemyBase
import datetime

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

    if True:
        #http://localhost:8000/newsfeed
        login_cur = db_sess.query(Feedcommunities)
        final = []
        for i in login_cur:
            info_user = db_sess.query(Communities).filter(Communities.id == i.id_communities).first()
            final.append({"information":  {"text":  i.text, "date": i.date, "like": i.like, "name" : info_user.name}})
        # final = sorted(final, key=lambda x: x[3])
        return {"flag": 1, "info": final}
    else:
        return {"flag": 0}

@app.route("/messenger", methods=['GET'])
def messenger():
    ID = session.get("id")
    if ID != -1:
        #http://localhost:8000/messenger
        search = "%{}%".format(ID)
        #db_sess = db_session.create_session()
        final = []
        login_cur = db_sess.query(Dialog).filter(Dialog.id_users.like(search))
        for i in login_cur:
            users = str(i.id_users).replace(str(ID), '').replace(',', "").split()
            name = db_sess.query(User).filter(User.id == users).first().name
            info = db_sess.query(Message).filter(Message.id_dialog == i.id)
            texts = sorted(list([j.id_user, j.text, j.data] for j in info), key=lambda x:x[2], reverse=True)


            
            # mes = [[j.id_user, j.text, j.data] for j in info]
            print(info)
            final.append({"name": name, "last_text": [j[1] for id, j in enumerate(texts) if id == 0][0]})
        return {"flag": 1, "dialog": final, "search": search, "ID" : ID}
    else:
        return {"flag": 0}

@app.route("/correspondence", methods=['POST', 'GET'])
def correspondence():
    #http://localhost:8000/correspondence?dialog=1
    ID = session.get("id")
    
    if request.method == 'POST' and ID != -1:
        #http://localhost:8000/correspondence?dialog=1&text=привет
        args = request.args
        dialog = args.get("dialog")
        text = args.get('text')
        #image = args.get("image") 
        #date = args.get("date")
        add_message = Message()
        add_message.id_dialog = int(dialog)
        add_message.id_user = int(ID)
        add_message.text = text
        add_message.data = datetime.datetime.now().date()
        #.strftime("%Y-%m-%d")
        db_sess.add(add_message)
        db_sess.commit()
        print('-------------------')
        return {"flag": 1}

    elif request.method == 'GET':
        if ID != -1:
            args = request.args
            id_dialog = args.get('dialog')
            print(id_dialog)
            #db_sess = db_session.create_session()
            login_cur = db_sess.query(Message).filter(Message.id_dialog == id_dialog)
            final = [[1 if i.id_user == ID else 0, i.text, i.data] for i in login_cur]
            final = sorted(final, key=lambda x: x[2])
            return {"flag": 1, "info": final}

        else:
            return {"flag": 0, "ID": ID}
    return {"flag": 0, "ID": ID}

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
    #http://localhost:8000/friends
    ID = session.get("id")
    if ID != -1:
        search = "%{}%".format(ID)
        login_cur = db_sess.query(Friends).filter(Friends.id_users.like(search))
        final = []
        for i in login_cur:
            users = str(i.id_users).replace(str(ID), '').replace(',', "").split()
            print(users)
            info = db_sess.query(User).filter(User.id == int(users[0])).first()
            final.append([info.name])
        final.sort()
        return {"flag": 1, "info": final}
    else:
        return {"flag": 0}

@app.route("/communities",methods=['POST', 'GET'])
def communities():
    ID = session.get("id")
    if ID != -1:
        #http://localhost:8000/communities
        login_cur = db_sess.query(Communities).all()
        final = [i.name for i in login_cur]
        return {"flag": 1, "info": final}
    else:
        return {"flag": 0}
    

@app.route("/feedcommunities",methods=['POST', 'GET'])
def feedcommunities():
    ID = session.get("id")
    if ID != -1:
        final = []
        args = request.args
        id_communities = args.get('communities')
        login_cur = db_sess.query(Feedcommunities).filter(Feedcommunities.id_communities == id_communities)
        #print(login_cur)
        for i in login_cur:
            name = db_sess.query(Communities).filter(Communities.id == i.id_communities).first().name
            final.append({"name": name, "text": i.text, "like": i.like, "date": i.date, "image": i.image})
    
        return {"flag": 1, "info": final}
    else:
        return {"flag": 0}


@app.route("/settings", methods=['GET', 'POST'])
def settings():
    ID = session.get("id")
    args = request.args
    exit = args.get('exit')
    theme = args.get('theme')
    vision = args.get('vision')
    if request.method == 'POST' and ID != -1:
        #http://localhost:8000/settings?exit=1&theme=1&vision=1
        
        if bool(exit):
            session['id'] = -1
            return {"flag": 1, "notes": "вышел из аккунта"} 
        else:
            login_cur = db_sess.query(Settings).filter(Settings.id_user == ID).first()
            login_cur.theme = theme
            login_cur.vision = vision
            db_sess.commit()
            return {"flag": 1, "notes": "поменял настройки"}
    elif request.method == 'GET':
        if ID != -1:
            login_cur = db_sess.query(Settings).filter(Settings.id_user == ID).first()

            return {"flag": 1, "theme": login_cur.theme, "vision": login_cur.vision}
        else:
            return {"flag": 0}
   
    

if __name__ == '__main__':
    app.run(port=8000, host='localhost')
