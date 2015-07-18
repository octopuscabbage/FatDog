import os
from flask.ext.api import FlaskAPI
import fitbark

app = FlaskAPI(__name__)

@app.route("/")
def hello():
    return 'Hello World!'
    
@app.route("/test")
def example():
    return {"yo":"it works"}

class fitbark_endpoints:
    fitbark_base = "/fitbark"
    dog_id_and_auth = "/<key>/<int:id>/"

    #actually usable ones
    dog_picture = fitbark_base + "/dog_picture" + dog_id_and_auth
    dog_info = fitbark_base + "/dog_info" + dog_id_and_auth
    dog_activity = fitbark_base + "/dog_activity" + dog_id_and_auth
    dog_goal = fitbark_base + "/daily_goal" + dog_id_and_auth

@app.route(fitbark_endpoints.dog_picture)
def dog_picture(key,id):
    return get_dog_picture(key,id)

@app.route(fitbark_endpoints.dog_info)
def dog_info(key,id):
    return get_dog_info(key,id)

@app.route(fitbark_endpoints.dog_activity)
def dog_activity(key,id):
    return get_dog_activity(key,id)

@app.route(fitbark_endpoints.dog_goal)
def dog_goal(key,id):
    return get_dog_goal(key,id)

