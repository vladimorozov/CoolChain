import pyodbc
import Matrix_Erstellen 
import Kontrolle
import Temperaturueberwachung

liste_DatenbankCoolChain = []
liste_DatenbankTemp = []
listeFehler =[]
listeWetter = []
liste_Neu = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] 

from datetime import timedelta
dtZeit10 = timedelta(
    hours=0,
    minutes=10,
    seconds=0
)
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

#die Datentabelle wird in einzelne Listen nach IDs unterteilt

Matrix_Erstellen.erstellen(liste_Neu,liste_DatenbankCoolChain)

neue_liste = [feld for feld in liste_Neu  if feld != []]  

eingabe = int(input("1: Kontrolle der Kühlkette\n2: Temperaturüberwachung\n3: Wetter\nWas möchtest du überprüfen:"))

if eingabe == 1:
    # Kontrolle ob alle 20 IDs aufgelistet sind        
    if len(neue_liste) < 20:
        print("\nEin oder mehrere Einträge fehlen\n")

    Kontrolle.stationsKontrolle(neue_liste,listeFehler,eingabe)

    Kontrolle.zeitKuehlung(neue_liste,dtZeit10,listeWetter,listeFehler,eingabe)

    Kontrolle.zeitGesamt(neue_liste,dtZeit48)

    Kontrolle.korrekt(neue_liste,listeFehler,listeWetter)

if eingabe == 2:
    Temperaturueberwachung.temp_Ueberwachung(liste_DatenbankTemp)

if eingabe == 3:

    Kontrolle.stationsKontrolle(neue_liste,listeFehler,eingabe)

    Kontrolle.zeitKuehlung(neue_liste,dtZeit10,listeWetter,listeFehler,eingabe)

        #hier kommt dann dein Programm Nico, die beiden Funktionen darüber sind für die IDs über 10 min
print(listeWetter)