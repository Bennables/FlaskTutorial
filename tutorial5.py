from flask import Flask, render_template, redirect, request, url_for, session
#sessions. All session data is encrypted
app = Flask(__name__)
app.secret_key = "Hello, I'm ben"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login/", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("name"))
    else:
        return render_template("login.html")
    
@app.route("/name")
def name():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
    
if __name__ == "__main__":
    app.run(debug = True)
