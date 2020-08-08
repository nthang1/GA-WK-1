# function find_user: finds user specified in argument, can provide keys for additional information

import requests
from requests_oauthlib import OAuth1

base_url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# search = '?q='

user_base_url = 'https://api.twitter.com/1.1/users/lookup.json'
user_search = '?screen_name='

auth = OAuth1()

def find_user(user, keys=None):
    results = requests.get(user_base_url + user_search + user.replace('@', ''), auth=auth).json()[0]

    if keys != None:
        reduced_results = {}
        for key in keys:
            reduced_results[key] = results[key]
        return reduced_results

    else:
        return results

find_user('@GA', keys=['name', 'screen_name', 'followers_count', 'friends_count'])
# find_user('@GA')