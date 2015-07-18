import os
from flask.ext.api import FlaskAPI

app = FlaskAPI(__name__)

@app.route("/")
def hello():
    return 'Hello World!'
    
@app.route("/test")
def example():
    return {"yo":"it works"}
