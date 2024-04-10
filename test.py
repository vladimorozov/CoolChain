import pyodbc
import Matrix_Erstellen 
import Kontrolle
liste_Datenbank = []
listeWetter =[]
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
iIndex_Liste1=0

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
    liste_Datenbank.append(a) #Matrix wird aus der Datentabelle übernommen   
# Verbindung schließen
cursor.close()
conn.close()

#die Datentabelle wird in einzelne Listen nach IDs unterteilt

Matrix_Erstellen.erstellen(liste_Neu,liste_Datenbank)

neue_liste = [feld for feld in liste_Neu  if feld != []]  


# Kontrolle ob alle 20 IDs aufgelistet sind        
if len(neue_liste) < 20:
    print("Ein oder mehrer Einträge fehlen")

Kontrolle.stationsKontrolle(neue_liste)

Kontrolle.zeitKuehlung(neue_liste,dtZeit10,listeWetter)

print(listeWetter)