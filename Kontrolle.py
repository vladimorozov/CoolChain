def stationsKontrolle(liste,liste_Fehler,eingabe): 
    for Liste in range (0, len(liste)):
        
        for station in range (0,len(liste[Liste])-2,2):
            #Variablen von der Liste werden übertragen
            transportStation1=liste[Liste][station][1]
            transportStation2=liste[Liste][station+1][1]
            transportStation3=liste[Liste][station+2][1]

            direction1 = liste[Liste][station][4]
            direction2 = liste[Liste][station+1][4]
            direction3 = liste[Liste][station+2][4]

            ergebnis = liste[Liste][0][2]

            #Bedingungen für fehlende Aus und Einscheck-Zeitpunkte.
            if transportStation1!=transportStation2 and transportStation3==transportStation2 and ergebnis not in liste_Fehler:
                liste_Fehler.append(ergebnis)
                if eingabe ==1:
                    print("ID: ",ergebnis,"|Aus- oder Eincheck-Zeitpunkt fehlt in der Mitte\n") 

            #Bedingung für fehlerhafte Transportstationen
            if transportStation1!=transportStation2 and direction1 == direction2 and ergebnis not in liste_Fehler: 
                liste_Fehler.append(ergebnis)
                if eingabe ==1:
                    print("ID: ",ergebnis,"|Fehler bei den Transportstationen\n")  

            #Bedingung für aus und wieder Einchecken im gleichen Kühllager
            if transportStation1==transportStation3 and direction1 == direction3 and ergebnis not in liste_Fehler: 
                liste_Fehler.append(ergebnis)
                if eingabe ==1:
                    print("ID: ",ergebnis,"|Aus und wieder Einchecken im gleichen Kühllager\n")    

            #Bedingung für doppelte Auschek-Zeitpunkte
            if transportStation3==transportStation2 and direction3 == direction2 and ergebnis not in liste_Fehler: 
                liste_Fehler.append(ergebnis)
                if eingabe ==1:
                    print("ID: ",ergebnis,"|Doppelter Auscheck-Zeitpunkt\n")   

        # BEdingung Auscheck-Zeitpunkt fehlen am Ende
        if len(liste[Liste]) % 2 !=0 and ergebnis not in liste_Fehler:
            liste_Fehler.append(ergebnis)
            if eingabe ==1:
                print("ID: ",ergebnis,"|Auscheck-Zeitpunkt fehlt am Ende da Tr. nicht abgeschlossen.\n")
                
    return liste_Fehler


def zeitKuehlung(liste,zeit,wetter,fehler,eingabe):
    
    for Liste in range (0, len(liste)):
    #Kontrolle Zeiträume ohne Kühlung
        for iOhne_Kuehlung in range(1,len(liste[Liste])-2,2):
            
            #Variablen werden übertragen
            transportzeit1 = liste[Liste][iOhne_Kuehlung][5]
            transportzeit2 = liste[Liste][iOhne_Kuehlung+1][5]

            #Zeitstempeln werden verglichen: Fehler bei einer Zeitdifferenz von über 10 Min
            if  transportzeit2 - transportzeit1 > zeit and liste[Liste][0][2] not in wetter  and liste[Liste][0][2] not in fehler:
                wetter.append([liste[Liste][0][2],liste[Liste][iOhne_Kuehlung][5],liste[Liste][iOhne_Kuehlung+1][5]])
                if eingabe == 1:
                    print("ID:",liste[Liste][0][2],"|Verifikation: Übergabe > 10 min\n")
                
                
    return liste,wetter

def zeitGesamt(liste,zeit):

    for iIndex in range (0,len(liste)):
        #Variablen werden übertragen
        transportAnfang = liste[iIndex][0][5]
        transportEnde   = liste[iIndex][len(liste[iIndex])-1][5]
        #Gesamtzeit wird kontrolliert: Fehler bei einer Zeit über 48h
        if transportEnde - transportAnfang > zeit:
            print("ID:",liste[iIndex][0][2],"|Verifikation: Transportdauer > 48h\n")

# Restliche Id's werden als korrekt identifiziert.
def korrekt(liste,fehler,wetter):
    for iIndex in range (0, len(liste)):
        if liste[iIndex][0][2] not in wetter and liste[iIndex][0][2] not in fehler:
            print("ID:",liste[iIndex][0][2],"|Verifikation: Korrekt\n")
