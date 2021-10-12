import sqlite3
from sqlite3.dbapi2 import IntegrityError

database = "database.db"

def get_users():
    sql = "SELECT id, username, pwhash FROM users"
    return select(sql)

def has_user(username, password):
    sql = "SELECT 1 FROM users WHERE username='"+username+"' AND pwhash='"+password+"'"
    result = select(sql)
    print(result)
    if result: return True
    return False

def add_user(username, pwhash):
    sql = "INSERT INTO users (username, pwhash) VALUES ('"+username+"', '"+pwhash+"')"
    try:
        insert(sql)
    except IntegrityError:
        return False
    return True

def select(sql):
    conn = sqlite3.connect(database)
    cursor = conn.execute(sql)
    list = cursor.fetchall()
    conn.close()
    return list

def insert(sql):
    conn = sqlite3.connect(database)
    conn.execute(sql)
    conn.commit()
    conn.close()
    