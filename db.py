import sqlite3
from sqlite3.dbapi2 import IntegrityError

database = "database.db"

# USERS
#-------------------
def get_users():
    sql = "SELECT id, username, pwhash FROM users"
    return select_all(sql)

def get_user_id(username, password):
    sql = "SELECT id FROM users WHERE username='"+username+"' AND pwhash='"+password+"'"
    id = select_one(sql)
    try:
        return id[0]
    except TypeError:
        return None

def add_user(username, pwhash, secret):
    sql = "INSERT INTO users (username, pwhash, secret) VALUES ('"+username+"', '"+pwhash+"', '"+secret+"')"
    try:
        return insert(sql)
    except IntegrityError:
        return None

def get_secret(id):
    sql = "SELECT secret FROM users WHERE id="+str(id)
    try:
        return select_one(sql)[0]
    except TypeError:
        return ""


#MESSAGES
#-------------------
def get_messages():
    sql = "SELECT message, username FROM messages, users WHERE messages.user_id=users.id LIMIT 100"
    return select_all(sql)

def add_message(id, message):
    sql = "INSERT INTO messages (user_id, message) VALUES ("+id+", '"+message+"')"
    insert(sql)

#-------------------

def select_all(sql):
    conn = sqlite3.connect(database)
    cursor = conn.execute(sql)
    list = cursor.fetchall()
    conn.close()
    return list

def select_one(sql):
    conn = sqlite3.connect(database)
    cursor = conn.execute(sql)
    list = cursor.fetchone()
    conn.close()
    return list

def insert(sql):
    conn = sqlite3.connect(database)
    id = conn.execute(sql).lastrowid
    conn.commit()
    conn.close()
    return id
    