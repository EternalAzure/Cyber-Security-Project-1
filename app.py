from flask import Flask
import secrets
''' Flaw 3: csrf solution
from flask_wtf.csrf import CSRFProtect
'''

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

''' Flaw 3: csrf solution
csrf = CSRFProtect()
csrf.init_app(app)
'''

import routes

''' Flaw 2: HTTPS solution
if __name__ == "__main__":
    app.run(ssl_context='adhoc')
'''

