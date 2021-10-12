from flask import Flask
import secrets
from os import getenv

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

import routes