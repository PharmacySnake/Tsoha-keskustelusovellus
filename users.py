from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from db import db


def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            #print(session)
            session["user_id"] = user.id
            session["username"] = username
            #print(session)
            return True
        else:
            return False


def user_id():
    return session.get("user_id", 0)


def logout():
    session.clear()


def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)
