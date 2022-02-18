from app import app
from flask import render_template, redirect, request, session

import users
import messages


@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", count=len(list), messages=list)
    '''
    if users.user_id() == 0:
        return redirect("/login")
    else:
        list = messages.get_list()
        return render_template("index.html", count=len(list), messages=list)
    '''

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    if messages.send(content):
        return redirect("/")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")


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
        if len(username) < 3:
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
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")


