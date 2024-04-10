def erstellen(neueListe,liste_Datenbank):
    iIndex_Liste_Neu =0
    for alteListe in range (0, len(liste_Datenbank)):
        if alteListe == 0:
            neueListe[0].append(liste_Datenbank[alteListe])

        elif neueListe[iIndex_Liste_Neu][0][2]== liste_Datenbank[alteListe][2]:
            neueListe[iIndex_Liste_Neu].append(liste_Datenbank[alteListe])

        else :
            iIndex_Liste_Neu +=1
            neueListe[iIndex_Liste_Neu].append(liste_Datenbank[alteListe])
    return neueListe