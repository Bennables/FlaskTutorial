from flask import Flask, redirect, url_for

# if app.route has / before and after, url can be with / or not


app = Flask(__name__)

#differnt page
#create route    
#prob should be /home but whatever
@app.route("/") 
def home():
    return "Hello, it's home <h3>hi<h3>"


#another page. This one will give us <name> as the param
#prints Hello (value of name) when at 127.0.0.1:5000/(value of name)
@app.route("/<name>/")
def user(name):
    return f"Hello {name}"

#demoing a redirect (cases where bad credentials)
@app.route("/admin/")
def admin():
    #can't use user yet
    return redirect(url_for("home"))

@app.route("/admin1/")
def admin1():
    print("redirected")
    return redirect(url_for("user", name = 'Admin1'))


if __name__ == "__main__":
    app.run()