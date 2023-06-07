from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content = [1,4,2,523])

@app.route("/<name>/")
def user(name):
    return render_template("index.html", content = name)

if __name__ == "__main__":
    app.run()