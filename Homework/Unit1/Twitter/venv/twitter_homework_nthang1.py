# function find_user: finds user specified in argument, can provide keys for additional information

import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
search = '?q='

user_base_url = 'https://api.twitter.com/1.1/followers/list.json'
user_search = '?screen_name='

auth = OAuth1('cAgAFtIDM0v3TQhF9XzL5E4kS', 'VO4HmlhY3quTguSaaTL8sO37sAM96LKLpC3OyFXoS8I78D4Ozz',
              '1291416908072353793-Awldljs5fDNbeaDUYJ0JD3FCNy5qXP', 'UNAhCbK67f9X3fxj2hxmzZVm9pLm5DJnZDSQPcQgrwWbC')

def find_user(user):
    if user[0] == '@':
        print(requests.get(user_base_url + user_search + user.replace('@', ''), auth=auth).json())
    else:
        print(requests.get(user_base_url + user_search + user, auth=auth).json())

find_user('GA')