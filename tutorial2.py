from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hallo <h1>DDDDD</h1>"

if __name__ == "__main__":
    app.run()