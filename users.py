from db import select_all, select_one, insert, update
from sqlite3.dbapi2 import IntegrityError
from hashlib import md5


def get_users():
    sql = "SELECT id, username, pwhash FROM users"
    return select_all(sql)

def verify_user(username, password):
    print("verify user")
    pw = hash(password)
    sql = f"SELECT id, username FROM users WHERE username='{username}' AND pwhash='{pw}'"
    print(sql)
    return select_one(sql)
    

def add_user(username, password, secret):
    print(username, password)
    # hash_value = generate_password_hash(password)
    hash_value = md5(password.encode('utf-8')).hexdigest()
    sql = "INSERT INTO users (username, pwhash, secret) VALUES ('"+username+"', '"+hash_value+"', '"+secret+"')"
    try:
        return insert(sql)
    except IntegrityError:
        return None

def get_secret(id):
    print("get_secret")
    sql = "SELECT secret FROM users WHERE id="+str(id)
    print(sql)
    try:
        return select_one(sql)[0]
    except TypeError:
        return ""

def change_secret(secret, id):
    print("change_secret()")
    print(secret)
    sql = "UPDATE users SET secret=:secret WHERE id=:id"
    bindings = {"secret": secret, "id": id}
    update(sql, bindings)

def check_password_hash(given_pw, existing_pw):
    if  existing_pw == hash(given_pw):
        return True
    return False

def hash(input):
    return md5(input.encode('utf-8')).hexdigest()