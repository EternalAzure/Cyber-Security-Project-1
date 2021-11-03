from db import select_all, insert
''' Flaw 3: xss solution
from flask import escape
'''

def get_messages():
    sql = "SELECT message, username FROM messages, users WHERE messages.user_id=users.id LIMIT 100"
    return select_all(sql)

def add_message(id, message):
    sql = "INSERT INTO messages (user_id, message) VALUES (:id, :message)"
    # Flaw 3: xxs
    bindings = {"id": id, "message": message}
    ''' Flaw 3: xxs solution
    bindings = {"id": id, "message": escape(message)}
    '''
    insert(sql, bindings)
