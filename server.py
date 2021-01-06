
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello(): 
    return "Yoga"


data = {
    "peter": {
        "username": "Peter Stradinger",
        "email": "peter.stradinger@logicmonitor.com",
        "poses": [
            {"name": "Downward Facing Dog"},
            {"name": "Upward Facing Dog"},
            {"name": "Shivasana"},
        ]
    },
    "athena": {
        "username": "Athena Partch",
        "email": "athena.partch@logicmonitor.com",
        "poses": [
            {"name": "Downward Facing Dog"},
            {"name": "Upward Facing Dog"},
            {"name": "Puppy Pose"},
        ]
    }
}



@app.route("/users/<username>")
def listUser(username):
    print (data)
    print (username)
    return data[username]
    
@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}!"
