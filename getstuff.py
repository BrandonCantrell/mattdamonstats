#!/usr/bin/python3
#Working with warcraftlogs API to play around
import json
import requests
from datetime import datetime as dt, timedelta

#Datemath bullshit
last_week = dt.now() - timedelta(days=7)
now_int = int(dt.now().timestamp() * 1000)
last_week_int = int(last_week.timestamp() * 1000)

#API Variables
api_token = 'c5eec3055c6db89b97b61ce74cf4eb1b'
api_url_base = 'https://www.warcraftlogs.com/v1/'
guild = 'matt damon'
realm = 'arthas'
region = 'US'

headers = {'Content-Type': 'application/json',
           'Authorization': f'{api_token}'}

def get_guild():
    api_url = f'https://www.warcraftlogs.com:443/v1/reports/guild/{guild}/{realm}/{region}?start={last_week_int}&end={now_int}&api_key={api_token}'
    response = requests.get(api_url, headers=headers)
    info = json.loads(response.content.decode('utf-8'))
    return info


print(json.dumps(get_guild(), indent=4))


