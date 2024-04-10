def stationsKontrolle(liste): 
    iIndex_Liste =0   
    while iIndex_Liste <len(liste):
        for iStation in range (0,len(liste[iIndex_Liste])-5,2):

        #Kontrolle von doppelten Lager Einträge

            transportStation1   = liste[iIndex_Liste][iStation][1]
            transportStation2   = liste[iIndex_Liste][iStation+1][1]
            direction1 = liste[iIndex_Liste][iStation][4]
            direction2 = liste[iIndex_Liste][iStation+1][4]
            if transportStation1!=transportStation2 and direction1 == direction2 :
                print("ID:",liste[iIndex_Liste][0][2],"|Stationen greifen ineinander\n")
                del liste[iIndex_Liste]
                iIndex_Liste = 0
    
        iIndex_Liste += 1
    return liste

def zeitKuehlung(liste,zeit,wetter):
    iIndex_Liste=0
    
    while iIndex_Liste <len(liste):
    #Kontrolle Zeiträume ohne Kühlung
        for iOhne_Kuehlung in range(1,len(liste[iIndex_Liste])-6,2):

            transportzeit1 = liste[iIndex_Liste][iOhne_Kuehlung][5]
            transportzeit2 = liste[iIndex_Liste][iOhne_Kuehlung+1][5]

            if  transportzeit2 - transportzeit1 > zeit:
                print("ID:",liste[iIndex_Liste][0][2],"|Verifikation: Übergabe > 10 min\n")
                wetter.append(liste[iIndex_Liste][0][2])
                del liste[iIndex_Liste]
                iIndex_Liste=0
        iIndex_Liste += 1
    return liste
    return wetter