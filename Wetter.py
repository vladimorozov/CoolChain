# Importieren der benötigten Bibliotheken
import requests 


# Definition der Funktion 'wetter'
def berechne_durchschnittemp_transport (transportstationen, dictionary,wetter,temperaturen):

    # Füllen des Wörterbuchs mit Transportstationsdaten
    for item in transportstationen:
        id, station, category, plz = item
        dictionary[station] = [id,category,plz]

    # API-Schlüssel für den Wetterdienst
    api_key = "UUS9ZE5GKTGY6D5T2TME2KXX5" 

    # Durchlaufen aller Wettereinträge
    for eintrag in wetter:

        # Extrahieren der notwendigen Daten aus dem Eintrag
        station_name = eintrag[3]
        datetime_obj = eintrag[1]
        datetime_obj2 = eintrag[2]
        transportID = eintrag [0]

        # Erstellen der Postleitzahl für die API-Anfrage
        postleitzahl = dictionary[station_name][2] + ",DE"

        # Bestimmen der Start- und Endstunde für die Durchschnittsberechnung
        start_hour = datetime_obj.hour
        end_hour = datetime_obj2.hour

        # Erstellen des Zeitstempels für die API-Anfrage
        timestamp = datetime_obj.strftime('%Y-%m-%dT%H:%M:%S') 

        # Erstellen der URL für die API-Anfrage
        url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{timestamp}'.format(location=postleitzahl, timestamp=timestamp) 

        # Senden der API-Anfrage und Speichern der Antwort
        response = requests.get(url, params={'unitGroup': 'metric','key': api_key,'include': 'hours'}) 

        # Umwandeln der Antwort in ein JSON-Objekt
        data = response.json() 

        # Initialisieren der Variablen für die Durchschnittsberechnung
        temp_sum = 0
        count = 0

        # Durchlaufen aller Stunden im gewünschten Zeitraum
        for hour in range(start_hour, end_hour+1):

            # Extrahieren der Temperatur für die aktuelle Stunde und Hinzufügen zur Summe
            temp = data['days'][0]['hours'][hour]['temp']
            temp_sum += temp
            count += 1

        # Berechnen der Durchschnittstemperatur
        avg_temp = round(temp_sum / count,1)

        # Hinzufügen der Durchschnittstemperatur zur Liste
        temperaturen.append([transportID, avg_temp])

        # Ausgabe der Durchschnittstemperatur
        print(f'Von dem Transport:\n {transportID}\n im Zeitraum:\n {datetime_obj}\n bis\n {datetime_obj2}\n Beträgt die Durchschnittstemperatur:\n {avg_temp} Grad Celsius.\n')

    # Rückgabe der Liste mit Durchschnittstemperaturen
    return temperaturen
