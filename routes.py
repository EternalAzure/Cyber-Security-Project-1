from flask import render_template, session, request, redirect
from flask.templating import render_template_string
from app import app


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/login", methods=["POST"])
def login():
    return
    #Do stuff if POST
    #
    #

@app.route("/none")
def none():
    return render_template_string('                                          \
    <!DOCTYPE html>                                                          \
        <head>                                                               \
        <title>Unsecure | info</title>                                       \
        <link rel="stylesheet" type="text/css" href="/static/index.css"/>    \
        <script>                                                             \
                                                                             \
        </script>                                                            \
        </head>                                                              \
        <body>                                                               \
          <div class="split right">                                          \
            <div class="centered">                                           \
                <form action="" method="POST">                               \
                    <input type="text" name="input">                         \
                    <input type="submit" value="Submit">                     \
                </form>                                                      \
            </div>                                                           \
          </div>                                                             \
        </body>                                                              \
    </html>                                                                  \
')
