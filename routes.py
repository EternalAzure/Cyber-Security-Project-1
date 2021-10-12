from flask import render_template, session, request, redirect
from flask.templating import render_template_string
from app import app
import db


@app.route("/", methods=["GET", "POST"])
def index():
    users = db.get_users()
    return render_template("index.html", users=users)

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/login", methods=["POST"])
def login():
    print("Did login")
    user = request.form["username"]
    password = request.form["password"]
    if db.has_user(user, password):
        session["username"] = user
    return redirect("/")


@app.route("/register", methods=["POST"])
def register():
    print("Did register")
    user = request.form["username"]
    password = request.form["password"]
    session["username"] = user
    db.add_user(user,password)
    return redirect("/")

@app.route("/logout", methods=["POST"])
def logout():
    print("Did logout")
    try:
        del session["username"]
    except KeyError:
        pass
    return redirect("/")

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
