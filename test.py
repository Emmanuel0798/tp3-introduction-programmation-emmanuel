import os 
import dataclasses
os.system("cls")

def transformInputCoordinate(coordinateInput) -> list:  # Fonction pour reçevoir les coordonnées sous forme "ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee" et
                                                        # le retourner en une liste simple de 4 colones
    coordinateInput.split(sep=",")
    coordinateInput[0].split(sep="-")
    coordinateInput[1].split(sep="-")
    return [coordinateInput[0][0], coordinateInput[0][1], coordinateInput[1][0], coordinateInput[1][1]]

