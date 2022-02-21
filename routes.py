from app import app
from flask import render_template, redirect, request, session

import users
import communicationManager

@app.route("/")
def index():
    #list = communicationManager.get_list()
    list = communicationManager.get_topics()
    return render_template("index.html", count=len(list), topics=list)
'''
@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    topic = request.form["topic"]

    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    elif len(content) > 5000:
        return render_template("error.html", message="Viesti on liian pitkä")
    elif communicationManager.send(content, topic):
        return redirect("/")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")
'''

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]

        if len(username) < 1:
            return render_template("error.html", message="Käyttäjänimi on liian lyhyt")
        elif len(username) > 23:
            return render_template("error.html", message="Käyttäjätunnus on liian pitkä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if len(password1) < 3:
            return render_template("error.html", message="Salasana on liian lyhyt")
        elif len(password1) > 32:
            return render_template("error.html", message="Salasana on liian pitkä")
        elif password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        print("tässä")
        if users.register(username, password1):
            print("tänne")
            return redirect("/")
        else:
            print("täällä")
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
'''
@add.route("/topic/<int:id>")
def topic(id):
    return render_template("thread.html", )
'''
'''
@add.route("/newtopic", methods=["GET", "POST"])
def create_new_topic():
    if request.method == "GET":
        return render_template("newtopic.html")
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        token = request.form["csrf_token"]

        if not check_token(token):
            abort(403)
        elif len(title) > 123:
            return render_template("error.html", message="Uuden viestiketjun aiheen nimi on liian pitkä")
        elif len(content) > 5000:
            return render_template("error.html", message="Viesti on liian pitkä")
        elif communicationManager.create_new_topic(title, content):
            return redirect("/")
        else:
            return render_template("error.html", message="Viestiketjun luominen ei onnistunut")
'''

def check_token(token):
    if session["csrf_token"] != token:
        return False
    return True

'''
@app.route("/profile/<int:id>")
def profile(id):
    allow = False
    if is_admin():
        allow = True
    elif is_user() and user_id() == id:
        allow = True
    elif user_id():
        sql = "SELECT 1 FROM friends WHERE user1=:user1 AND user2=:user2"
        result = db.session.execute(sql, {"user1":user_id(), "user2":id})
        if result.fetchone():
            allow = True
    if not allow:
        return render_template("error.html", message="Ei oikeutta nähdä sivua")
'''
'''
@app.route("/update", method=["POST"])
def update():
    check_user()
    user_id = session["user_id"]
    email = request.form["email"]
    sql = "UPDATE users SET email=:email WHERE id=:user_id"
    db.session.execute(sql, {"email":email, "user_id":user_id})
'''
'''
@app.route("/result", methods=["POST"]) #XSS haavoittuvuus
def result():
    name = request.form["name"]
    return "Moikka, "+name

@app.route("/result", methods=["POST"]) #ei XSS haavoittuvuutta
def result():
    name = request.form["name"]
    return render_template("result.html", name=name)
'''
