#!/usr/bin/env python
import requests
import sys
import os
import pprint

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

# from main.models import Genres
from django.conf import settings

# city = 'Provo'
# payload = {'APPID': settings.WEATHER_API_KEY, 'units': 'imperial'}

# get_current_weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s' % (city), params=payload)

# current_weather_dict = get_current_weather.json()

pp = pprint.PrettyPrinter(indent=4)

# pp.pprint(current_weather_dict)

# temp = current_weather_dict['main']['temp']

# pp.pprint(temp)

api_key = settings.FORCAST_API_KEY
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
