import os
import dataclasses
os.system("cls") 


# --- Constance : ---
TABLEROW = 6 
TABLECOLUMN = 6
NBRBOATS = 3    # Nombre de bateau que chaque joueur peut posséder au début de la partie


# --- Variable dans le code principale : ---
namePlayer1 = ""
namePlayer2 = "" 
quit = False    # Si à True, alors on quitte le jeux et on ferme le programme


# --- Fonction : ---
def transformInputCoordinate(coordinateInput) -> list:  # Fonction pour reçevoir les coordonnées sous forme "ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee" et
                                                        # le retourner en une liste simple de 4 colones
    coordinateInput.split(sep=",")
    coordinateInput[0].split(sep="-")
    coordinateInput[1].split(sep="-")
    return [coordinateInput[0][0], coordinateInput[0][1], coordinateInput[1][0], coordinateInput[1][1]]

def displayGrid(self) -> None:     # Fonction pour afficher la grille actuelle du joueur 
    print()
    for row in self.grille :
        print(f"    {row}")
    print()


# --- Création de la classe Joueur : ---
@dataclasses.dataclass 
class Joueur : 
    name : str 
    grille = []     # L'état actuelle du plateau du joueurs

    def __post_init__(self) -> None:   # Cette fonciton initialise les dimensions du pateau et les coordonnées des bateaux lors de la création d'un object Joueur
        coordinateInput = ""    # Coordonné entre par le joueur sous forme "ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee"
        coordinateTranform = [] # Coordonné entre par le joueur qui a été transformer en des coordonné manipulable

        self.grille = [TABLECOLUMN * [0] for i in range(TABLEROW)]  
        
        print("Voici votre grille de jeux : ") 
        displayGrid(self) 
        for i in len(NBRBOATS) : 
            print(f"{self.name}, entre la position de ton bateau #{i + 1} : (ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee)")
            coordinateInput = input(" > ")
            coordinateTranform = transformInputCoordinate(coordinateInput)

            


# --- Création de la classe coordonnee : --- 
@dataclasses.dataclass 
class Coordonnee :
    coordinateInput : str   # Coordonnées tel que entrer par le joueurs
    coordinateLine1 : int   # Coordonnées manipulable
    coordinateColumn1 : int     # Coordonnées manipulable
    coordinateLine2 : int   # Coordonnées manipulable optionnel (lors d'un simple tir, on a pas besoin)
    coordinateColumn2 : int     # Coordonnées manipulable optionnel (lors d'un simple tir, on a pas besoin)


# --- Début du jeux :  ---
print("Veuillez entrer le nom du premier joueur : ")
namePlayer1 = input(" > ") 
print("\nVeuillez entrer le nom du deuxième joueur : ")
namePlayer2 = input(" > ")
os.system("cls")
player1 = Joueur(namePlayer1) 
player2 = Joueur(namePlayer2)

while not quit == True :    # Boucle principale du jeux
    print()