from flask import Flask, render_template, request, session, redirect
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False  # if True, the session will be permanent and use cookies to store data
app.config["SESSION_TYPE"] = "filesystem"  # store session data on the server's filesystem, not in cookies
Session(app)  # initialize the session


@app.route("/")
def index():
    return render_template("index.html", name=session.get("username"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
