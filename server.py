from flask import Flask, render_template, send_from_directory, request
import authController
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

@app.route("/img/<creator>/<imgname>", methods=["GET", "POST"])
def imgpage(creator,imgname):
    found = authController.storeInHistory(creator,imgname)
    if not found:
        return "The meme you are looking for does not exist"
    return 'Received ' + imgname + ' by ' + creator
    # return '<image src="FIGURE_ME_OUT.jpg">'

if __name__ == "__main__":
    app.run(debug=True)
