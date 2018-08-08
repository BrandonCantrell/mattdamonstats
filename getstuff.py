#!/usr/bin/python3
#Working with warcraftlogs API to play around
import json
import requests
from datetime import date

api_token = 'redacted'
api_url_base = 'https://www.warcraftlogs.com/v1/'

headers = {'Content-Type': 'application/json',
           'Authorization': f'{api_token}'}

def get_guild():
    api_url = f'https://www.warcraftlogs.com:443/v1/reports/guild/matt%20damon/arthas/US?api_key={api_token}'
    response = requests.get(api_url, headers=headers)
    info = json.loads(response.content.decode('utf-8'))
    return info


print(json.dumps(get_guild(), indent=4))


