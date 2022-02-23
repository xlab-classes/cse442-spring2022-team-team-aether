import os
import re
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def root():
    return render_template('index.html')

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

@app.route("/styles")
def styles():
    return render_template('styles.css')

@app.route("/search")
def search():
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)