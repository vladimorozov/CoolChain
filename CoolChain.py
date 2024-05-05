#Import der einzelnen Funktionen
import pyodbc
import Wetter
import Matrix_Erstellen 
import Kontrolle
import Temperaturueberwachung
import decryption
#Erstellung von bestimmten Listen
liste_DatenbankCoolChain = []
liste_DatenbankTemp = []
listeFehler =[]
listeWetter = []
liste_Neu = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

liste_DatenbankTransportstation = []
liste_Temperatren = []
#Wörterbuch erstellen
transportstation_dict = {}
#Zeit für die 10min
from datetime import timedelta
dtZeit10 = timedelta(
    hours=0,
    minutes=10,
    seconds=0
)
#Zeit für die 48h
dtZeit48 = timedelta(
    days=2,
    hours=0,
    minutes=0,
    seconds=0
)

# Verbindungsdaten
server = 'sc-db-server.database.windows.net'
database = 'supplychain' # Setze den Namen deiner Datenbank hier ein
username = 'rse'
password = 'Pa$$w0rd'
# Verbindungsstring
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)
# Verbindung herstellen
conn = pyodbc.connect(conn_str)
# Cursor erstelneue_listelen
cursor = conn.cursor()
# SQL-Statement ausführen
cursor.execute('SELECT * FROM v_coolchain order by transportID,datetime')
# Ergebnisse ausgeben
for row in cursor:
    a = row
    liste_DatenbankCoolChain.append(a) #Matrix wird aus der Datentabelle übernommen
# Verbindung schließen
cursor.close()



cursor2 = conn.cursor()
cursor2.execute('SELECT * FROM v_tempdata')
for row in cursor2:
    b = row
    liste_DatenbankTemp.append(b)   
cursor2.close()
conn.close()

#Transportstation
#cursor3 = conn.cursor()
#cursor3.execute('SELECT * FROM transportstation')
#for row in cursor3:
#    c = row
#    liste_DatenbankTransportstation.append(c)
#cursor3.close()
decryption.decrypt_db(liste_DatenbankTransportstation)





#die Datentabelle wird in einzelne Listen nach IDs unterteilt
Matrix_Erstellen.erstellen(liste_Neu,liste_DatenbankCoolChain)

#Matrix wird in eine neue Liste gebracht um Leere Stellen zu entfernen
neue_liste = [feld for feld in liste_Neu  if feld != []]  

#Eingabe für die Kontrollauswahl
eingabe = int(input("1: Kontrolle der Kühlkette\n2: Temperaturüberwachung\n3: Wetter Transporte über 10 min\nWas möchtest du überprüfen:"))

#Auswahl Vergleich für Stationskontrolle
if eingabe == 1:
    # Kontrolle ob alle 20 IDs aufgelistet sind        
    if len(neue_liste) < 20:
        print("\nEin oder mehrere Einträge fehlen\n")

    #Kontrolle der Stationen
    Kontrolle.stationsKontrolle(neue_liste,listeFehler,eingabe)
    
    #Kontrolle der Kühlungszeiten
    Kontrolle.zeitKuehlung(neue_liste,dtZeit10,listeWetter,listeFehler,eingabe)
    
    #Kontrolle der Gesamtzeiten
    Kontrolle.zeitGesamt(neue_liste,dtZeit48)

    #Kontrolle von den Korrekten IDs
    Kontrolle.korrekt(neue_liste,listeFehler,listeWetter)

#Auswahl für die Temperaturüberwachung
if eingabe == 2:
    Temperaturueberwachung.temp_Ueberwachung(liste_DatenbankTemp)

#Auswahl Wetter
if eingabe == 3:

    Kontrolle.stationsKontrolle(neue_liste,listeFehler,eingabe)

    Kontrolle.zeitKuehlung(neue_liste,dtZeit10,listeWetter,listeFehler,eingabe)

    Wetter.berechne_durchschnittemp_transport(liste_DatenbankTransportstation,transportstation_dict,listeWetter,liste_Temperatren)

