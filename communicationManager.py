from db import db
import users

def get_list():
    sql = "SELECT M.content, U.username, M.sent_at FROM messages M, users U WHERE M.user_id=U.id ORDER BY M.id"
    result = db.session.execute(sql)
    return result.fetchall()

def send(content, topic_id):
    if users.user_id == 0:
        return False
    
    sql = "INSERT INTO messages (content, user_id, topic_id, sent_at) VALUES (:content, :users.user_id(), :topic_id NOW())"
    db.session.execute(sql, {"content":content, "user_id":users.user_id(), "topic_id":topic_id})
    db.session.commit()
    return True


def get_topics():
    sql = "SELECT title, user_id, creation_time FROM topics WHERE visible = True ORDER BY creation_time"
    result = db.session.execute(sql)
    topics = result.fetchall()
    return topics

def create_new_topic(title, content):
    if users.user_id() == 0:
        return False

    sql = "INSERT INTO topics (title, user_id, creation_time, visible) VALUES (:title, :user_id, NOW(), 1)"
    result = db.session.execute(sql, {"title":title, "user_id":user_id})
    topic_id = result.fetchone[0]
    db.session.commit()
    send(content, topic_id)
    return True
