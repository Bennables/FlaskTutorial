from flask import Flask

app = Flask(__name__)

#differnt page
#create route    
#prob should be /home but whatever
@app.route("/") 
def home():
    return "Hello, it's home <h3>hi<h3>"

if __name__ == "__main__":
    app.run()