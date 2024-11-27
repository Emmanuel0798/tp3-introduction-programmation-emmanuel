import os 
import dataclasses
os.system("cls")

def transformInputCoordinate(coordinateInput) -> list:  # Fonction pour reçevoir les coordonnées sous forme "ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee" et
                                                        # le retourner en une liste qui contient deux listes qui chacune de ces list son des coordonnées "ligne, colonne"
    coordinateInput = coordinateInput.split(sep=",")
    coordinateInput[0] = coordinateInput[0].split(sep="-")
    coordinateInput[1] = coordinateInput[1].split(sep="-")
    for i in coordinateInput :
        for j in i :
            coordinateInput[i][j] = int(coordinateInput[i][j])
    return [coordinateInput[0], coordinateInput[1]]

print(transformInputCoordinate("1-2,3-4"))
