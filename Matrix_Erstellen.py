#Hier wird die 3D Matrix erstellt: [2D Matrix][Liste][Spalte]
def erstellen(neueListe,liste_Datenbank):
    iIndex_Liste_Neu =0

    for alteListe in range (0, len(liste_Datenbank)):
        if alteListe == 0:
            #erste ID wird übernommen
            neueListe[0].append(liste_Datenbank[alteListe])
            #Alle gleichen IDs werden in die gleiche Liste übernommen
        elif neueListe[iIndex_Liste_Neu][0][2]== liste_Datenbank[alteListe][2]:
            neueListe[iIndex_Liste_Neu].append(liste_Datenbank[alteListe])

        else :
            #Die Liste wird auf die nächste Liste gebracht sobald eine andere ID auftaucht
            iIndex_Liste_Neu +=1
            neueListe[iIndex_Liste_Neu].append(liste_Datenbank[alteListe])
    return neueListe