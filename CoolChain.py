import pyodbc

liste_Datenbank = []
liste_Neu = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] 
iIndex_Liste_Neu = 0
iIndex_Liste1    = 0
iIndex_Liste2    = 0
iIndex_Liste3    = 0
iIndex_Liste4    = 0

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
# Cursor erstellen
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

for iIndex_Liste_Alt in range (0, len(liste_Datenbank)):
    if iIndex_Liste_Alt == 0:
        liste_Neu[0].append(liste_Datenbank[iIndex_Liste_Alt])

    elif liste_Neu[iIndex_Liste_Neu][0][2]== liste_Datenbank[iIndex_Liste_Alt][2]:
        liste_Neu[iIndex_Liste_Neu].append(liste_Datenbank[iIndex_Liste_Alt])

    else :
        liste_Neu[iIndex_Liste_Neu+1].append(liste_Datenbank[iIndex_Liste_Alt])
        iIndex_Liste_Neu +=1


# Kontrolle ob alle 20 IDs aufgelistet sind        
if len(liste_Neu)<20:
    print("\nEine oder mehrere Transport IDs fehlen\n")
#Es wird nach fehlenden oder doppelte directions überprüft
while iIndex_Liste1 <len(liste_Neu):
    for iStation in range (0,len(liste_Neu[iIndex_Liste1])-3):

        #Kontrolle von doppelten Lager Einträge

        transportStation1   = liste_Neu[iIndex_Liste1][iStation][1]
        transportStation2   = liste_Neu[iIndex_Liste1][iStation+2][1]
        transportRichtung1  = liste_Neu[iIndex_Liste1][iStation+1][4] 
        transportRichtung2  = liste_Neu[iIndex_Liste1][iStation+2][4]

        if transportStation1==transportStation2 and transportRichtung1 !=transportRichtung2:
            print("ID:",liste_Neu[iIndex_Liste1][0][2],"|Verifikation: Aus und wieder Einchecken im gleichen Lager\n")
            del liste_Neu[iIndex_Liste1]
            iIndex_Liste1 = 0


    for iZeit_Stempel in range (0,len(liste_Neu[iIndex_Liste1])-2):

        #Kontrolle auf doppelte Einträge/Austräge
            
        transportStation1  = liste_Neu[iIndex_Liste1][iZeit_Stempel][1] 
        transportStation2  = liste_Neu[iIndex_Liste1][iZeit_Stempel+1][1]
        transportRichtung1 = liste_Neu[iIndex_Liste1][iZeit_Stempel][4]
        transportRichtung2 = liste_Neu[iIndex_Liste1][iZeit_Stempel+1][4]

        if transportRichtung1 == transportRichtung2:
            if transportStation1==transportStation2:
                if transportRichtung1 == "'out'":
                    print("ID:",liste_Neu[iIndex_Liste1][0][2],"|Verifikation: Doppelter Austrag\n")
                else:  
                    print("ID:",liste_Neu[iIndex_Liste1][0][2],"|Verifikation: Doppelter Eintrag\n")
                
            else: #Kontrolle auf fehlende Einträge innerhalb der ID Tabelle
                print("ID:",liste_Neu[iIndex_Liste1][0][2],"|Verifikation: Eintrag fehlt in der Mitte\n")

            del liste_Neu[iIndex_Liste1]
            iIndex_Liste1=0    
        
    #Kontrolle von fehlenden Einträge am Ende
    if  len(liste_Neu[iIndex_Liste1])%2!=0:
        print("ID:",liste_Neu[iIndex_Liste1][0][2],"|Verifikation: Eintrag fehlt am Anfang oder am Ende\n")
        del liste_Neu[iIndex_Liste1]
        iIndex_Liste1=0      

    #index Liste neu wird erhöht
    iIndex_Liste1 += 1

while iIndex_Liste2 <len(liste_Neu):
    #Kontrolle Zeiträume ohne Kühlung
    for iOhne_Kuehlung in range(1,len(liste_Neu[iIndex_Liste2])-2,2):

        transportzeit1 = liste_Neu[iIndex_Liste2][iOhne_Kuehlung][5]
        transportzeit2 = liste_Neu[iIndex_Liste2][iOhne_Kuehlung+1][5]

        if  transportzeit2 - transportzeit1 > dtZeit10:
            print("ID:",liste_Neu[iIndex_Liste2][0][2],"|Verifikation: Übergabe > 10 min\n")
            del liste_Neu[iIndex_Liste2]
            iIndex_Liste2=0
    iIndex_Liste2 += 1


#Kontrolle Transportdauer
while iIndex_Liste3 <len(liste_Neu):

    transportAnfang = liste_Neu[iIndex_Liste3][0][5]
    transportEnde   = liste_Neu[iIndex_Liste3][len(liste_Neu[iIndex_Liste3])-1][5]

    if transportEnde - transportAnfang > dtZeit48:
        print("ID:",liste_Neu[iIndex_Liste3][0][2],"|Verifikation: Transportdauer > 48 min\n")
        del liste_Neu[iIndex_Liste3]
        iIndex_Liste3=0  
    else:
        iIndex_Liste3 += 1

#verbleibende IDs werden als Korrekt gekenntzeichnet
while iIndex_Liste4 <len(liste_Neu):
    print("ID:",liste_Neu[iIndex_Liste4][0][2],"|Verifikation: Korrekt\n")
    iIndex_Liste4=iIndex_Liste4+1