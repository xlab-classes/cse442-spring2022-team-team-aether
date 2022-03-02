import os
import re
import flask
from flask import Flask, render_template, send_from_directory
app = Flask(__name__)


@app.route("/index")
@app.route("/")
def root():
    return render_template("index.html")


@app.route("/make")
def make():
    return render_template("make.html")


@app.route('/static/frontEngine')
def send_engine(path):
    return send_from_directory('js', path)

@app.route('/static/styles')
def send_styles(path):
    return send_from_directory('css', path)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/createaccount")
def createaccount():
    return render_template('createaccount.html')

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
    app.run(debug=True)