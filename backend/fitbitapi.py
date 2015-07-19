from flask import Flask, request
from flask_restful import Resource, Api
import fitbit
import json
import datetime
consumer_key = 'bb9e358028304057825d8a01b44bdc47'
consumer_secret = 'ca6cb45ff7af4c869d2987b7384a5184'
encoded_user_id = '36CRJ7'
oauth_token = '16723100b0e0f204b95702101223ee15'
oauth_token_secret = '8e7f56ee1d4a64713606ee10a80fd08c'

app = Flask(__name__)
api = Api(app)
human = fitbit.Fitbit(consumer_key, consumer_secret, resource_owner_key=oauth_token, resource_owner_secret=oauth_token_secret)

class get_human(Resource):
	def get(self):
		data = human.time_series('activities/steps', period='max')
		goal_steps = human.activities_daily_goal()['goals']['steps']
		outlist = []
		for entry in data["activities-steps"]:
			output_dict = {"date": entry["dateTime"], "activity": entry["value"], "target": goal_steps}
			outlist.append(output_dict)
		return [{"log": outlist}]

api.add_resource(get_human, '/human')


if __name__ == '__main__':
	app.run(debug=True)