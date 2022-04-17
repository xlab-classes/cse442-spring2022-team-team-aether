import re
from flask import Flask, render_template, send_from_directory, request, make_response, redirect, url_for
from re import template
from flask import Flask, render_template, send_from_directory, request
import authController
import datetime
import secrets

import generate

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def root():
    return render_template("index.html")

@app.route("/make", methods=["GET", "POST"])
def make():
    if request.method == "GET":
        return render_template("make.html")
    else:
        data = request.form.to_dict()
        print(data["templates"])
        print(data["TextColor"])
        print(data["FirstText"])
        print(data["SecondText"])
        username = request.cookies["User"]
        token = request.cookies["AuthToken"]
        if (authController.verifyToken(username, token)):
            generate.generate_image(username, data["templates"], data["FirstText"], data["SecondText"], data["TextColor"])
            return "sucessfully made image"
        else:
            return redirect(url_for("login"))

@app.route('/static/frontEngine')
def send_engine(path):
    return send_from_directory('js', path)

@app.route('/static/styles')
def send_styles(path):
    return send_from_directory('css', path)

@app.route('/static/samplememe')
def send_samplememe():
    return send_from_directory("jpg", "/static/samplememe")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        data = request.form.to_dict()
        username = data["Username"]
        password = data["Password"]
        if (authController.authlogin(username, password)):
            key = secrets.token_urlsafe()
            authController.updateToken(username, key)
            resp = make_response(render_template('account.html'))
            resp.set_cookie("AuthToken", key, expires=datetime.datetime.now() + datetime.timedelta(days=30))
            resp.set_cookie("User", username, expires=datetime.datetime.now() + datetime.timedelta(days=30))
            return resp
        else:
            return "Login Failed, Incorrect username or Password"

@app.route("/createaccount", methods=["GET","POST"])
def createaccount():
    if request.method == "GET":
        return render_template('createaccount.html')
    elif request.method == "POST":
        data = request.form.to_dict()
        username = data["Username"]
        password = data["Password"]
        if (authController.authcreateAccount(username, password)):
            return render_template('account.html')
        else:
            return "Account Creation Failed, try another name or password"
@app.route("/popular")
def popular():
    return render_template('popular.html')

@app.route("/account")
def account():
    user = request.cookies.get("User")
    token = request.cookies.get("AuthToken")
    if(user == None or token == None):
        print("redirect")
        return redirect(url_for("login"))
    if authController.verifyToken(user, token):
        return render_template('account.html', username=user)
    else:
        print("non valid")
        return redirect(url_for("login"))

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/logout")
def logout():
    resp = make_response(render_template('account.html'))
    resp.set_cookie("AuthToken", "", expires=datetime.datetime.now())
    resp.set_cookie("User", "", expires=datetime.datetime.now())
    return resp

# @app.route("/img/<creator>/<imgname>", methods=["GET", "POST"])
# def imgpage(creator,imgname):
#     #found = historydb.storeInHistory(creator,imgname)
#     if not found:
#         return "The meme you are looking for does not exist"
#     return 'Received ' + imgname + ' by ' + creator
#     # return '<image src="FIGURE_ME_OUT.jpg">'

if __name__ == "__main__":
    con = ("cert.pem", "key.pem")
    app.run(ssl_context=con)
