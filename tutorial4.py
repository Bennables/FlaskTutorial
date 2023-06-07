from flask import Flask, url_for, redirect, render_template
#posting and getting  
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login/", methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route("/<usr>/")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)