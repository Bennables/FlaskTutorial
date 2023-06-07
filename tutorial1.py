from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

#create route    
@app.route("/") #prob should be /home but whatever
#differnt page
def home():
    return "Hello, it's home <h3>hi<h3>"