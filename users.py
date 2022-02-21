from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from db import db
import secrets


def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

def user_id():
    return session.get("user_id", 0)

def is_admin():
    id = user_id()
    if user_id:
        sql = "SELECT is_admin FROM users WHERE user_id=:id"
        result = db.session.execute(sql, {"user_id":id})
        return result.fetchone()
    return False

def logout():
    session.clear()

def register(username, password):
    hash_value = generate_password_hash(password)
    stature = "FALSE"
    print("u: "+username + ", p: "+password)
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password, :is_admin)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
        sql = "SELECT * FROM users"
        result = db.session.execute(sql)
        print(result.fetchall)
    except:
        return False
    return login(username, password)
