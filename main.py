from flask import Flask, request
from scripts import *
import requests

test = {"login": "user", "password" : "1234", "password2": "1234", "name": "", "email":""}
ENTRANCE = False
ID = -1
app = Flask(__name__)

@app.route('/authorization', methods=['GET'])
def login():
    args = request.args
    login = args.get('login')
    password = args.get('password')
    if len(login) and len(password):
        if check_user(login, password):
            ID = get_id(login)
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
    if not (isvalid_login(login)):
        return {"flag": 0}
    if  isvalid_value(login, password, name):
        base, cursor = connect_base()
        cursor.execute(
            f"""INSERT INTO users (login, password, name, role, email) VALUES ('{login}', '{password}', '{name}', 1, '{email}')""")
        base.commit()
        base.close()
        return {"flag": 1}
    else:
        return {"flag": 3} #не все поля заполнины
    

@app.route("/map", methods=['GET'])
def map():
    pass

@app.route("/newsfeed", methods=['GET'])
def newsfeed():
    if ID != -1:
        pass
    else:
        return {"flag": 0}

@app.route("/messenger", methods=['GET'])
def messenger():
    if ID != -1:
        pass
    else:
        return {"flag": 0}

@app.route("/correspondence", methods=['GET'])
def correspondence():
    if ID != -1:
        pass
    else:
        return {"flag": 0}

@app.route("/other", methods=['GET'])
def other():
    if ID != -1:
        pass
    else:
        return {"flag": 0}

@app.route("/profile", methods=['GET'])
def profile():
    if ID != -1:
        pass
    else:
        return {"flag": 0}

@app.route("/friends", methods=['GET'])
def friends():
    if ID != -1:
        pass
    else:
        return {"flag": 0}

@app.route("/communities", methods=['GET'])
def communities():
    if ID != -1:
        pass
    else:
        return {"flag": 0}

@app.route("/settings", methods=['GET'])
def settings():
    if ID != -1:
        pass
    else:
        return {"flag": 0}
    

if __name__ == '__main__':
    app.run(port=8000, host='localhost')
