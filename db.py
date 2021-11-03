import sqlite3
from multipledispatch import dispatch

database = "database.db"

def select_all(sql):
    conn = sqlite3.connect(database)
    cursor = conn.execute(sql)
    list = cursor.fetchall()
    conn.close()
    return list

@dispatch(str)
def select_one(sql):
    conn = sqlite3.connect(database)
    cursor = conn.execute(sql)
    list = cursor.fetchone()
    conn.close()
    return list

@dispatch(str, dict)
def select_one(sql, bindings):
    conn = sqlite3.connect(database)
    cursor = conn.execute(sql, bindings)
    list = cursor.fetchone()
    conn.close()
    return list

def insert(sql, bindings):
    print(sql)
    conn = sqlite3.connect(database)
    id = conn.execute(sql, bindings).lastrowid
    conn.commit()
    conn.close()
    return id

def update(sql, bindings):
    conn = sqlite3.connect(database)
    conn.execute(sql, bindings)
    conn.commit()
    conn.close()



    