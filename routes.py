from os import getenv
from flask import render_template, session, request, redirect, flash
from flask.helpers import make_response
import requests
from app import app
import messages as m
import users
import re

mock_API_KEY = getenv("mock_API_KEY")

@app.route("/")
def index():
    messages = m.get_messages()
    return render_template("index.html.j2", messages=messages)

@app.route("/change")
def change():
    secret = request.args.get("secret")
    user_id = request.args.get("user_id")
    users.change_secret(secret, user_id)
    return redirect(f"/person/{user_id}")

@app.route("/person/<int:id>")
def person(id):
    ''' Flaw 1: Credentials solution
    if session["user_id"] != id:
        flash("You have to log in before entering personal page")
        return redirect("/")
    '''
    
    if not "language" in session:
        session["language"] = "english"

    messages = m.get_messages()
    secret = users.get_secret(id)
    if session["language"] == "english":
        return render_template("person_en.html.j2", messages=messages, secret=secret, id=id)
    return render_template("person_fi.html.j2", messages=messages, secret=secret, id=id)

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/send", methods=["POST"])
def send():
    message = request.form["message"]
    user_id = request.form["id"]
    m.add_message(user_id, message)
    return redirect(f"/person/{user_id}")

# Flaw 5: SSRF
@app.route("/language", methods=["GET"])
def language():
    api = request.args.get("api")
    ref = request.args.get("ref")

    # Call to mock server
    mock_response = requests.get(f"http://localhost:5000/{mock_API_KEY}{api}")

    # Do stuff with mock_response
    session["language"] = mock_response.text
    return redirect(ref)

''' Flaw 5: ssrf solution
def language():
    index = request.args.get("language_index")
    id = request.args.get("id")
    
    if type(id) != int:
        flash("Personal page id was not a number")
        return redirect("/")

    ref = f"/person/{id}"

    languages = [english, finnish]
    language = languages[index]
    # Call to mock server
    mock_response = requests.get(f"http://localhost:5000/{mock_API_KEY}/api/language?lan={language}")

    # Do stuff with mock_response
    session["language"] = mock_response.text
    return redirect(ref)
'''

#LOGGING STUFF
#-------------------
@app.route("/login", methods=["POST"])
def login():
    user = request.form["username"]
    password = request.form["password"]
    # user[0] is id and user[1] is username
    user = users.verify_user(user, password)
    if user:
        '''Flaw 1: Credentials solution
        session["user_id"] = user[0]
        '''
        session["username"] = user[1]
        return redirect(f"/person/{user[0]}")
    
    flash("Wrong username or message")
    return redirect("/")


@app.route("/register", methods=["POST"])
def register():
    user = request.form["username"]
    password = request.form["password"]
    secret = request.form["secret"]
    ''' Flaw 4: weak password solution
    regex = "/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{9,}$/g"
    format = re.compile(regex)  
    k = re.search(format, password)
    if k is None :
        flash("Vaaditaan iso ja pieni kirjain sekä numero. Vähintään 9 merkiä pitkä")
    '''
    id = users.add_user(user, password, secret)
    if id == None:
        flash("Username is taken")
        return redirect("/")

    session["username"] = user
    return redirect("/person/"+str(id))

@app.route("/logout", methods=["POST"])
def logout():
    try:
        del session["username"]
    except KeyError:
        pass
    return redirect("/")


# MOCK UP SERVER
#-------------------
# Mock up API in some far away external server
@app.route(f"/{mock_API_KEY}/api/language")
def internal_language():
    language = request.args.get("lan")
    print("lan=", language)
    # Do stuff
    #
    #
    return make_response(language)
    
# Mock up API in some far away external server
@app.route(f"/{mock_API_KEY}/api/admin")
def admin():
    return make_response("mock response from /admin")
