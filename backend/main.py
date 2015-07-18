import os
from flask import Flask

app = Flask (__name__)

@app.route("/")
def hello():
    return 'Hello World!'
    
@app.route("/test")
def example():
    return {"yo":"it works"}
