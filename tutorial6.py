from flask import Flask, render_template, redirect, request, url_for, session, flash
#Message flashing
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "Hello, I'm ben"
app.permanent_session_lifetime = timedelta(minutes = 5) #can be minutes, secs

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login/", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True   #this line makes the session permanent
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        else:
            return render_template("login.html")
    
@app.route("/user/")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
    
@app.route("/logout/")
def logout():
    if "user" in session:
        user = session["user"]
        flash("Logged out successfully" + user, "info") #second param is a category, google for more
    session.pop("user", None)
    
    return redirect(url_for("login"))
    
if __name__ == "__main__":
    app.run(debug = True)
