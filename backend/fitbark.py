import requests
import json
from util import *

test_token = "29deef75ecf5b43d012d05bec21b43acba0c20215350930e9ac9890e966d5ceb"
test_dog = 1727

def get_dog_data(token):
    ''''Gets Dog Objects based on a users token'''
    dogs = get_related_dogs(token)
    dog_dicts = map(lambda d: {'name': d['dog']['name'],'id':d['dog']['id'] },dogs['dog_relations'])
    for dog in dog_dicts:
       dog['log'] = []
       activity_series = get_activity_series(token,dog['id']) 
       if('status' in activity_series):
           #Means there isn't any data
           continue

       for entry in activity_series['activity_series']['records']:
           dog['log'].append({'date' : entry['date'], 'activity' : entry['activity_value'], 'target' : entry['daily_target'], 'percent_done' : float(entry['activity_value']) / float(entry['daily_target']) * 100, 'min_play': entry['min_play'], 'min_active' : entry['min_active'], 'min_rest' : entry['min_rest']})
    return dog_dicts
    
class endpoints:
    base =  "http://app.fitbark.com/api/v1/"
    dog_info = base + "dog/" 
    dog_goal = base + "daily_goal/"
    dog_picture = base + "picture/dog/"
    related_dogs = base + "dog_relations"
    activity_log = base + "activity_series"
    
def get_activity_series(token,dog_id):
    post_data = __make_post_data(dog_id)
    header = make_header(token)
    header["Content-Type"] = "application/json"
    response = requests.post(endpoints.activity_log,headers=header,data=post_data)
    return __guarded_json_load(response.text)
    
def __make_post_data(id):
    return json.dumps({"activity_series": {"dog_id": str(id),"from": str(n_months_ago(1)), "to" : str(current_date()),'resolution':'DAILY' }} )
    

def __guarded_json_load(text):
    if(text != u' '):
        return json.loads(text)
    else:
        return bad_status()

def bad_status():
    return json.dumps({"status":"BAD"})

def make_get_request(token,endpoint,dog_id,json_response=True):
    response = requests.get(endpoint + str(dog_id),headers=make_header(token))
    if (json_response):
        return json.loads(response.text)
    else:
        return response

def make_header(bearer_token):
    return {"Authorization": "Bearer " + bearer_token, "Accept": "application/json"}

def get_dog_info(bearer_token,dog_id):
    header = make_header(bearer_token)
    response = requests.get(endpoints.dog_info + str(dog_id), headers=make_header(bearer_token))
    out = json.loads(response.text)
    return out

def get_activity(bearer_token,dog_id):
    header = make_header(bearer_token)
    dog_activity = {}
    response = requests.get(endpoints.dog_info + str(dog_id), headers=make_header(bearer_token))
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
    

def get_related_dogs(bearer_token):
    return make_get_request(bearer_token,endpoints.related_dogs,"")
