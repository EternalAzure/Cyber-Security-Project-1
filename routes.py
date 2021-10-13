from flask import render_template, session, request, redirect, flash
from app import app
import db


@app.route("/")
def index():
    messages = db.get_messages()
    return render_template("index.html", messages=messages)

@app.route("/person/<int:id>")
def person(id):
    messages = db.get_messages()
    secret = db.get_secret(id)
    return render_template("person.html", messages=messages, secret=secret, id=id)

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/send", methods=["POST"])
def send():
    message = request.form["message"]
    user_id = request.form["id"]
    db.add_message(user_id, message)
    return redirect("/person/"+str(user_id))

#LOGGING STUFF
#-------------------
@app.route("/login", methods=["POST"])
def login():
    print("Did login")
    user = request.form["username"]
    password = request.form["password"]
    id = db.get_user_id(user, password)
    if id:
        session["username"] = user
        return redirect("/person/"+str(id))
    return redirect("/")


@app.route("/register", methods=["POST"])
def register():
    print("Did register")
    user = request.form["username"]
    password = request.form["password"]
    secret = request.form["secret"]
    id = db.add_user(user, password, secret)

    if id == None:
        flash("Username is taken")
        return redirect("/")

    session["username"] = user
    return redirect("/person/"+str(id))

@app.route("/logout", methods=["POST"])
def logout():
    print("Did logout")
    try:
        del session["username"]
    except KeyError:
        pass
    return redirect("/")
