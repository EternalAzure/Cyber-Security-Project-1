from flask import Flask
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

import routes

''' Flaw 2: HTTPS solution
if __name__ == "__main__":
    app.run(ssl_context='adhoc')
'''
