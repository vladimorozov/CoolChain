import pyodbc
import Temperaturueberwachung


liste_Temperatur = []
liste_Datenbank = []
ausahl = int(input("1 oder 2:"))
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
# Cursor erstellen
cursor = conn.cursor()
# SQL-Statement ausführen
cursor.execute('SELECT * FROM v_tempdata')
# Ergebnisse ausgeben
for row in cursor:
    a = row
    liste_Temperatur.append(a)
    #Matrix wird aus der Datentabelle übernommen   
# Verbindung schließen
cursor.close()
cursor = conn.cursor()
# SQL-Statement ausführen
cursor.execute('SELECT * FROM coolchain')
# Ergebnisse ausgeben
for row in cursor:
    b = row
    liste_Datenbank.append(b) #Matrix wird aus der Datentabelle übernommen   
# Verbindung schließen
cursor.close()
conn.close()


if ausahl ==1:
    Temperaturueberwachung.temp_Ueberwachung(liste_Temperatur)
