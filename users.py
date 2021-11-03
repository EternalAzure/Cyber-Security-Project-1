from db import select_all, select_one, insert, update
from sqlite3.dbapi2 import IntegrityError
from hashlib import md5


def get_users():
    sql = "SELECT id, username, pwhash FROM users"
    return select_all(sql)

def verify_user(username, password):
    pw = hash(password)
    # Flaw 3: sql
    sql = f"SELECT id, username FROM users WHERE username='{username}' AND pwhash='{pw}'"
    ''' Flaw 3: sql solution
    sql = "SELECT id, username FROM users WHERE username=:username AND pwhash=:pw"
    bindings = {"username": username, "pwhash": pw}
    return select_one(sql, bindings)
    '''
    return select_one(sql)
    

def add_user(username, password, secret):
    hash_value = hash(password)
    sql = "INSERT INTO users (username, pwhash, secret) VALUES (:username, :pwhash, :secret)"
    bindings = {"username": username, "pwhash": hash_value, "secret": secret}
    try:
        return insert(sql, bindings)
    except IntegrityError:
        return None

def get_secret(id):
    sql = "SELECT secret FROM users WHERE id=:id"
    bindings = {"id": id}
    try:
        return select_one(sql, bindings)[0]
    except TypeError:
        return ""

def change_secret(secret, id):
    sql = "UPDATE users SET secret=:secret WHERE id=:id"
    bindings = {"secret": secret, "id": id}
    update(sql, bindings)

def check_password_hash(given_pw, existing_pw):
    if  existing_pw == hash(given_pw):
        return True
    return False


def hash(input):
    ''' Flaw 2: passwordhash solution
    return generate_password_hash(password)
    '''
    # Flaw 2: passwordhash
    return md5(input.encode('utf-8')).hexdigest()