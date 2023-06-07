from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login/", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("name", nam = user))
    else:
        return render_template("login.html")
    
@app.route("/<nam>/")
def name(nam):
    return render_template("loginAnswer.html", namer = nam)
    
if __name__ == "__main__":
    app.run(debug = True)
