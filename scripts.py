import sqlite3


def connect_base():
    base = sqlite3.connect('data/base.db')
    cursor = base.cursor()
    return base, cursor


def check_user(login, password):
    base, cursor = connect_base()
    user = cursor.execute(
        f"""SELECT * FROM users WHERE login = '{login}' AND password = '{password}'""").fetchall()
    base.close()
    if len(user) != 0:
        return user[0][0]
    return 0


def isvalid_login(login):
    base = sqlite3.connect('data/base.db')
    cursor = base.cursor()
    all_login = cursor.execute(f"""SELECT * FROM users WHERE login = '{login}'""").fetchall()
    base.close()
    if len(all_login) != 0:
        return False

    return True


def isvalid_password(first, second):
    if first == second:
        return True
    return False

def isvalid_value(*value):
    for i in value:
        if len(i) == 0:
            return False
    else:
        return True
