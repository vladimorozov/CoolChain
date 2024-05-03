import requests 
import json 
from datetime import datetime 

def woerterbuch (transportstationen, dictionary,wetter,temperaturen):
    


    for item in transportstationen:
        id, station, category, plz = item
        dictionary[station] = [id,category,plz]

    api_key = "ZYKSTLSASNBZ5MDNERF9Y5Z7E" 
    

    for eintrag in wetter:

        station_name1 = eintrag[3]
        datetime_obj = eintrag[1]
        transportID = eintrag [0]
        print(eintrag[0])

        postleitzahl = dictionary[station_name1][2] + ",DE"
        hour = datetime_obj.hour

        timestamp = datetime_obj.strftime('%Y-%m-%dT%H:%M:%S') 

        url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{timestamp}'.format(location=postleitzahl, timestamp=timestamp) 
        response = requests.get(url, params={'unitGroup': 'metric','key': 
        api_key,'include': 'hours'}) 
        data = response.json() 

        temp = data['days'][0]['hours'][hour]['temp']

        temperaturen.append([transportID,temp])

        print(f"Die Temperatur in der {hour}. Stunde ist {temp} Grad Celsius.")

    return temperaturen
