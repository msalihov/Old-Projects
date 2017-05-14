import urllib
import json
import config
from utility_functions import irc_functions


def run(self, target, location):
    couldrun = True
    try:
        autocomplete_url = 'http://autocomplete.wunderground.com/aq?query=' + location
        autocomplete_data = urllib.urlopen(autocomplete_url)
        autocomplete_json = json.loads(autocomplete_data.read())
    except Exception:
        irc_functions.say(self, 'Error while auto-completing location!', target)
        couldrun = False
    try:
        if couldrun:
            city_zmw = autocomplete_json['RESULTS'][0]['zmw']
            city_name = autocomplete_json['RESULTS'][0]['name']
    except Exception:
        irc_functions.say(self, 'Auto-complete could not find a match for ' + location, target)
        couldrun = False
    try:
        if couldrun:
            query_url = 'http://api.wunderground.com/api/' + config.get(
                'wund_api') + '/forecast/q/zmw:' + city_zmw + '.json'
            query_data = urllib.urlopen(query_url)
            query_json = json.loads(query_data.read())
    except Exception:
        irc_functions.say(self, 'Error while fetching data from API!', target)
        couldrun = False
    try:
        if couldrun:
            dayforecast = query_json['forecast']['simpleforecast']['forecastday'][0]
            result = ""
            result += city_name + ": "
            result += 'Sky Conditions: ' + dayforecast['conditions'] + ", "
            result += 'Temperature: low: ' + dayforecast['low']['celsius'] + "C/" + dayforecast['low'][
                'fahrenheit'] + "F, "
            result += 'high: ' + dayforecast['high']['celsius'] + "C/" + dayforecast['high']['fahrenheit'] + "F, "
            result += "Humidity: " + str(dayforecast['avehumidity']) + "%  "
            result += "(http://www.wunderground.com/q/zmw:" + city_zmw + ")"
            irc_functions.say(self, result, target)
    except Exception:
        irc_functions.say(self, 'Error while parsing data from API!', target)
        couldrun = False