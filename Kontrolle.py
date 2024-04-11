def stationsKontrolle(liste,liste_Fehler): 
    for Liste in range (0, len(liste)):
        
        for station in range (0,len(liste[Liste])-2,2):

            transportStation1=liste[Liste][station][1]
            transportStation2=liste[Liste][station+1][1]
            transportStation3=liste[Liste][station+2][1]

            direction1 = liste[Liste][station][4]
            direction2 = liste[Liste][station+1][4]
            direction3 = liste[Liste][station+2][4]

            ergebnis = liste[Liste][0][2]
            if ergebnis not in liste_Fehler:
                if transportStation1!=transportStation2 and transportStation3==transportStation2 :
                    liste_Fehler.append(ergebnis)
                    print("ID: ",ergebnis,"|Aus- oder Eincheck-Zeitpunkt fehlt in der Mitte\n") 

                if transportStation1!=transportStation2 and direction1 == direction2 :
                    liste_Fehler.append(ergebnis)
                    print("ID: ",ergebnis,"|Fehler bei den Transportstationen\n")  

                if transportStation1==transportStation3 and direction1 == direction3: 
                    liste_Fehler.append(ergebnis)
                    print("ID: ",ergebnis,"|Aus und wieder Einchecken im gleichen Kühllager\n")    

                if transportStation3==transportStation2 and direction3 == direction2: 
                    liste_Fehler.append(ergebnis)
                    print("ID: ",ergebnis,"|Doppelter Auscheck-Zeitpunkt\n")   

                if len(liste[Liste]) % 2 !=0:
                    liste_Fehler.append(ergebnis)
                    print("ID: ",ergebnis,"|Auscheck-Zeitpunkt fehlt am Ende da Tr. nicht abgeschlossen.\n")
                
    return liste_Fehler


def zeitKuehlung(liste,zeit,wetter,fehler):
    
    for Liste in range (0, len(liste)):
    #Kontrolle Zeiträume ohne Kühlung
        for iOhne_Kuehlung in range(1,len(liste[Liste])-2,2):
            
            transportzeit1 = liste[Liste][iOhne_Kuehlung][5]
            transportzeit2 = liste[Liste][iOhne_Kuehlung+1][5]

            if  transportzeit2 - transportzeit1 > zeit and liste[Liste][0][2] not in wetter  and liste[Liste][0][2] not in fehler:
                print("ID:",liste[Liste][0][2],"|Verifikation: Übergabe > 10 min\n")
                wetter.append(liste[Liste][0][2])
                
    return liste
    return wetter

def zeitGesamt(liste,zeit):

    for iIndex in range (0,len(liste)):

        transportAnfang = liste[iIndex][0][5]
        transportEnde   = liste[iIndex][len(liste[iIndex])-1][5]

        if transportEnde - transportAnfang > zeit:
            print("ID:",liste[iIndex][0][2],"|Verifikation: Transportdauer > 48 min\n")

def korrekt(liste,fehler,wetter):
    for iIndex in range (0, len(liste)):
        if liste[iIndex][0][2] not in wetter and liste[iIndex][0][2] not in fehler:
            print("ID:",liste[iIndex][0][2],"|Verifikation: Korrekt\n")
