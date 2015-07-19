import os
from flask.ext.api import FlaskAPI
from fitbark import get_dog_data
from fitbitapi import get_human, human_oauth

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

@app.route("/fitbit/<public>/<secret>/")
def get_human_oauth(public,secret):
    return human_oauth(public,secret)
    
@app.route("/fitbit/")
def human_data():
    return get_human()
