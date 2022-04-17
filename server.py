import re
import sys
from traceback import print_tb
from flask import Flask, render_template, send_from_directory, request, make_response, redirect, url_for
from re import template
from flask import Flask, render_template, send_from_directory, request
import authController
import generate
from imagestore import getimg

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
            print("token verified/")
            name = generate.generate_image(username, data["templates"], data["FirstText"], data["SecondText"], data["TextColor"])
            byte = getimg(username, name)
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
        authController.authlogin(username, password)
        return render_template('account.html')
@app.route("/createaccount", methods=["GET","POST"])
def createaccount():
    if request.method == "GET":
        return render_template('createaccount.html')
    elif request.method == "POST":
        data = request.form.to_dict()
        username = data["Username"]
        password = data["Password"]
        authController.authcreateAccount(username, password)
        return render_template('account.html')
@app.route("/popular")
def popular():
    return render_template('popular.html')

@app.route("/account")
def account():
    return render_template('account.html')

@app.route("/search")
def search():
    return render_template('search.html')


if __name__ == "__main__":
    con = ("cert.pem", "key.pem")
    app.run(host="cheshire.cse.buffalo.edu", port="4639",ssl_context=con)
