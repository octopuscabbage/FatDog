import os
from flask.ext.api import FlaskAPI
from fitbark import get_dog_data

app = FlaskAPI(__name__)

@app.route("/")
def hello():
    return 'Hello World!'
    
@app.route("/test")
def example():
    return {"yo":"it works"}

@app.route("/fitbark/<token>")
def dog_data(token):
    return get_dog_data(token)

