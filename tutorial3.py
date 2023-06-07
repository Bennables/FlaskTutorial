from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("indexTut3.html")

@app.route("/two/")
def two():
    return render_template("indexTut3-2.html")

if __name__ == "__main__":
    app.run(debug = True)