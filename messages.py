from db import select_all, insert

def get_messages():
    sql = "SELECT message, username FROM messages, users WHERE messages.user_id=users.id LIMIT 100"
    return select_all(sql)

def add_message(id, message):
    sql = "INSERT INTO messages (user_id, message) VALUES (:id, :message)"
    bindings = {"id": id, "message": message}
    insert(sql, bindings)
