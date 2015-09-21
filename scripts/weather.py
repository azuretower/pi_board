#!/usr/bin/env python
import requests
import sys
import os
import pprint
from time import sleep

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from django.conf import settings

pp = pprint.PrettyPrinter(indent=4)

api_key = settings.FORCAST_API_KEY
while True:
    os.system('clear')
    lat = '40.2181'
    lon = '-111.6133'
    get_forcast_weather = requests.get('https://api.forecast.io/forecast/%s/%s,%s' % (api_key, lat, lon))

    current_forcast_dict = get_forcast_weather.json()

    temp = current_forcast_dict['currently']['temperature']
    low = current_forcast_dict['daily']['data'][0]['temperatureMin']
    high = current_forcast_dict['daily']['data'][0]['temperatureMax']

    print 'Current: ' + str(temp)
    print 'High: ' + str(high)
    print 'Low: ' + str(low)

    sleep(120)
