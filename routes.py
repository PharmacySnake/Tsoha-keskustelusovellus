from app import app
from flask import render_template, redirect, request, session

import users
import communicationManager

@app.route("/")
def index():
    try:
        list = communicationManager.get_topics()
        return render_template("index.html", count=len(list), topics=list)
    except:
        return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    topic_id = request.form["topicid"]

    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    elif len(content) > 5000:
        return render_template("error.html", message="Viesti on liian pitkä")
    elif communicationManager.send(content, topic_id):
        return redirect("/topic/"+topic_id)
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
            print("success")
            return redirect("/")
        else:
            print("no worky")
            return render_template("error.html", message="Rekisteröinti ei onnistunut")


@app.route("/newtopic", methods=["GET", "POST"])
def newtopic():
    if request.method == "GET":
        return render_template("newtopic.html")

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        token = request.form["csrf_token"]

        if not users.check_token(token):
            abort(403)
        elif len(title) > 123:
            return render_template("error.html", message="Uuden viestiketjun aiheen nimi on liian pitkä")
        elif len(content) > 5000:
            return render_template("error.html", message="Viesti on liian pitkä")
        elif communicationManager.newtopic(title, content):
            return redirect("/")
        else:
            return render_template("error.html", message="Viestiketjun luominen ei onnistunut")


@app.route("/topic/<int:id>")
def topic(id):
    topic_nfo = communicationManager.topic(id)
    messages_list = communicationManager.get_messages_in_topic(id)
    return render_template("topic.html", topic=topic_nfo, count=len(messages_list), messages=messages_list)

