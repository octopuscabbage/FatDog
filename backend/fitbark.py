import requests
import json

class endpoints:
    dog_info = "http://app.fitbark.com/api/dog/" 
    dog_goal = "https://app.fitbark.com/api/v1/daily_goal/"
    dog_picture = "https://app.fitbark.com/api/v1/picture/dog/"
    
def make_get_request(token,endpoint,dog_id,json_response=True):
    header = make_header(token)
    response = requests.get(endpoint + str(dog_id),headers=payload)
    if (json_response):
        return json.loads(response.text)
    else:
        return response

def make_header(bearer_token):
    return {"Authorization": "Bearer " + bearer_token, "Accept": "application/json"}


def get_dog_info(bearer_token,dog_id):
    header = make_header(bearer_token)
    response = requests.get(dog_info + str(dog_id), headers=payload)
    out = json.loads(response.text)
    return out

def get_activity(bearer_token,dog_id):
    header = make_header(bearer_token)
    dog_activity = {}
    response = requests.get(dog_info + str(dog_id), headers=payload)
    out = json.loads(response.text)
    name = out["dog"]["name"]
    activity = out["dog"]["activity_value"]
    dog_activity["id"] = dog_id
    dog_activity["name"] = out["dog"]["name"]
    dog_activity["activity_value"] = out["dog"]["activity_value"]
    dog_activity["breed"] = out["dog"]["breed1"]["name"]
    dog_activity["fitbarkid"] = out["dog"]["bluetooth_id"]
    print len(out["dog"]["medical_conditions"])
    if len(out["dog"]["medical_conditions"]) > 0:
        dog_activity["medicalinfo"] = out["dog"]["medical_conditions"][0]["id"]
    else:
        dog_activity["medicalinfo"] = 0
        dog_activity["dob"] = out["dog"]["birth"]
        return dog_activity

def get_daily_goal(bearer_token,dog_id):
    return make_get_request(bearer_token,endpoints.dog_goal,dog_id)
    
def get_dog_picture(bearer_token,dog_id):
    return make_get_request(bearer_token,endpoints.dog_picture,dog_id)
    
