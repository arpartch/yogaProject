
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello(): 
    return "Yoga"


data={
      'athena': {'poses': ["cobra", "downdog"]}, 
      'peter': {'poses': ["updog", "childspose", "impossible"]},
      'adam': {'poses': ["cobra", "updog"]},
      'ethan': {'poses': ["updog", "downdog"]}, 
          }



@app.route("/users/<username>")
def listUser(username):
    print (data)
    print (username)
    return data[username]
    
@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}!"
