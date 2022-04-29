from email.mime import image
from email.parser import BytesHeaderParser
import re
import sys
from traceback import print_tb
from flask import Flask, render_template, send_from_directory, request, make_response, redirect, url_for
from re import template
from flask import Flask, render_template, send_from_directory, request
import authController
import historydb
import datetime
import secrets
import searchEngine
import io
from PIL import Image

import generate
import imagestore

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def root():
    posts = imagestore.getall()
    content = generate.generate_home(posts)
    print(content)

    return render_template("index.html", posts = content)

@app.route("/hash/<bytehash>")
def hashes(bytehash):
    print("in hashes")
    sys.stdout.flush()
    real = bytehash.replace(".jpg", '')
    bb = request.view_args
    #print("in hashes")
    print(real)
    sys.stdout.flush()

    imme = imagestore.imgbyhash(real)
    #print(imme)
    sys.stdout.flush()
    image = Image.open(io.BytesIO(imme))
    image.save('temp.jpg')
    send_from_directory('temp.jpg')


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
        print(data["tags"])
        username = request.cookies["User"]
        token = request.cookies["AuthToken"]
        if (authController.verifyToken(username, token)):
            print("token verified/")
            tags = generate.get_tags(data["tags"])
            name = generate.generate_image(username, data["templates"], data["FirstText"], data["SecondText"], data["TextColor"], tags)
            byte = imagestore.getuserimg(username, name)
            response = make_response(byte)
            response.headers.set('Content-Type', 'image/jpeg')
            response.headers.set('Content-Disposition', 'attachment', filename='%s.jpg' % "yourmeme")
            return response
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

@app.route('/generationFiles/drake.jpg')
def send_drake():
    return send_from_directory("generationFiles","drake.jpg")

@app.route('/generationFiles/trade.jpg')
def send_trade():
    return send_from_directory("generationFiles","trade.jpg")

@app.route('/generationFiles/cheating.jpg')
def send_cheating():
    return send_from_directory("generationFiles","cheating.jpg")

@app.route('/generationFiles/uno.jpg')
def send_uno():
    return send_from_directory("generationFiles","uno.jpg")

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

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        return None
    else:
        query = ["bag"]
        print(searchEngine.search(query))
        return render_template('search.html')

@app.route("/logout")
def logout():
    resp = make_response(render_template('account.html'))
    resp.set_cookie("AuthToken", "", expires=datetime.datetime.now())
    resp.set_cookie("User", "", expires=datetime.datetime.now())
    return resp

@app.route("/img/<creator>/<imgname>", methods=["GET", "POST"])
def imgpage(creator,imgname):
    username = request.cookies["User"]
    token = request.cookies["AuthToken"]
    if (authController.verifyToken(username, token)):
        found = historydb.storeInHistory(creator,imgname,username)
        if not found:
            return "The meme you are looking for does not exist"
        return 'Received ' + imgname + ' by ' + creator
        # return '<image src="FIGURE_ME_OUT.jpg">'
    return "You are not a registered user"

if __name__ == "__main__":
    con = ("cert.pem", "key.pem")
    app.run(ssl_context=con)
    #app.run(debug=True)
