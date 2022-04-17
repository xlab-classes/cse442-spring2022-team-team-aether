from flask import Flask, render_template, send_from_directory, request, make_response, redirect, url_for
import authController
import datetime
import secrets
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


if __name__ == "__main__":
    app.run(debug=True)
