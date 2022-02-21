from db import db
from flask import session
from sqlalchemy.sql import text
import users

def get_list():
    sql = "SELECT M.content, U.username, M.sent_at FROM messages M, users U WHERE M.user_id=U.id ORDER BY M.id"
    result = db.session.execute(sql)
    return result.fetchall()

def send(content, topic_id):
    if users.user_id == 0:
        return False

    user_id = users.user_id()
    sql = "INSERT INTO messages (content, user_id, topic_id, sent_at) VALUES (:content, :user_id, :topic_id, NOW())"
    db.session.execute(sql, {"content":content, "user_id":user_id, "topic_id":topic_id})
    db.session.commit()
    return True


def get_topics():
    sql = "SELECT T.id, T.title, U.username, T.creation_time FROM topics T, users U WHERE T.user_id=U.id ORDER BY T.creation_time" #AND visible IS TRUE
    result = db.session.execute(sql)
    return result.fetchall()

def newtopic(title, content):
    if users.user_id() == 0:
        return False

    user_id = users.user_id()
    sql = "INSERT INTO topics (title, user_id, creation_time) VALUES (:title, :user_id, NOW()) RETURNING id"
    result = db.session.execute(sql, {"title":title, "user_id":user_id})
    db.session.commit()
    topic_id = result.fetchone()[0]
    send(content, topic_id)
    return True

def topic(topic_id):
    topic_id = str(topic_id)
    sql = text("SELECT id, title, user_id, creation_time FROM topics T WHERE T.id=:id")
    result = db.session.execute(sql, {"id":topic_id})
    return result.fetchone()

def get_messages_in_topic(topic_id):
    topic_id = str(topic_id)
    sql = text("SELECT M.content, U.username, M.sent_at FROM messages M LEFT JOIN users U ON M.user_id = U.id WHERE M.topic_id=:id ORDER BY M.id")
    result = db.session.execute(sql, {"id":topic_id})
    return result.fetchall()
