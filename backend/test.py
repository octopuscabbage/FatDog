import fitbit
from pprint import pprint
import datetime
consumer_key = 'bb9e358028304057825d8a01b44bdc47'
consumer_secret = 'ca6cb45ff7af4c869d2987b7384a5184'
encoded_user_id = '36CRJ7'
oauth_token = '16723100b0e0f204b95702101223ee15'
oauth_token_secret = '8e7f56ee1d4a64713606ee10a80fd08c'

unauth_client = fitbit.Fitbit('bb9e358028304057825d8a01b44bdc47', 'ca6cb45ff7af4c869d2987b7384a5184')
# certain methods do not require user keys
#print unauth_client.food_units()

authd_client = fitbit.Fitbit(consumer_key, consumer_secret, resource_owner_key=oauth_token, resource_owner_secret=oauth_token_secret)

# pprint(authd_client.activities_list())
#prints daily goal
pprint(authd_client.user_profile_get())