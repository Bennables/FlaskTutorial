from flask import Flask, redirect, url_for

app = Flask(__name__)

#differnt page
#create route    
#prob should be /home but whatever
@app.route("/") 
def home():
    return "Hello, it's home <h3>hi<h3>"


#another page. This one will give us <name> as the param
#prints Hello (value of name) when at 127.0.0.1:5000/(value of name)
@app.route("/<name>")
def user(name):
    return f"Hello {name}"

#demoing a redirect (cases where bad credentials)
@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()