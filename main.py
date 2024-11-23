from flask import Flask
from scripts import *

test = {"login": "user", "password" : "1234", "password2": "1234", "name": "user", "email":"213123"}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if len(test["login"]) and len(test["password"]):
        if check_user(test["login"], test["password"]):
            return "yes"
        else:
            return "not user"
    else:
        return "not"
    
@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if not (isvalid_login(test["login"])):
        return "Уже есть такое пользователь"
    if  isvalid_password(test["password"], test["password2"]) and isvalid_value(test["login"], test["password"], test["password2"]):
        base, cursor = connect_base()
        cursor.execute(
            f"""INSERT INTO users (login, password, name, role, email) VALUES ('{test["login"]}', '{test["password"]}', '{test["name"]}', 1, '{test["email"]}')""")
        base.commit()
        base.close()
        return "Успешно"
    elif not (isvalid_password(test["password"],  test["password2"])):
        return 'Пароли не совпадают'
    else:
        return 'Заполни все поля!!!!'

if __name__ == '__main__':
    app.run(port=8000, host='localhost')
