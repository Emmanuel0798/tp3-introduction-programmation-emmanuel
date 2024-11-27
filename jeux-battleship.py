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
                                                        # le retourner en une liste qui contient deux listes qui chacune de ces list son des coordonnées "ligne, colonne"
    coordinateInput = coordinateInput.split(sep=",")
    coordinateInput[0] = coordinateInput[0].split(sep="-")
    coordinateInput[1] = coordinateInput[1].split(sep="-")

    for i, contenueI in enumerate(coordinateInput) :    # Les boucles "for" imbriquées servent simplement en tranformer les chiffres, qui sont en str, en int
        for j, contenuJ in enumerate(contenueI) :
            coordinateInput[i][j] = int(coordinateInput[i][j])
    return [coordinateInput[0], coordinateInput[1]]

    # VALIDATION DES COORDONNÉES : !!!!!!!!!!!!!!

def displayGrid(self) -> None:     # Fonction pour afficher la grille actuelle du joueur 
    print()
    for row in self.grille :
        for column in row : 
            print(f"[ {column} ]", end = "")
        print()


# --- Création de la classe Joueur : ---
@dataclasses.dataclass 
class Joueur : 
    name : str 
    grille = []     # L'état actuelle du plateau du joueurs

    def __post_init__(self) -> None:   # Cette fonciton initialise les dimensions du pateau et les coordonnées des bateaux lors de la création d'un object Joueur
        coordinateInput = ""    # Coordonné entre par le joueur sous forme "ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee"
        coordinateTransform = []     # Les coordonnées entre par le joueur pour un bateau qui a été transformer par la fonction "transformInputCoordinate()"
                                     # en des coordonnées manipulable

        self.grille = [TABLECOLUMN * [0] for i in range(TABLEROW)]  
        
        print("Voici votre grille de jeux : ") 
        displayGrid(self) 
        for i in range(NBRBOATS) : 
            print(f"{self.name}, entre la position de ton bateau #{i + 1} : (ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee)")
            coordinateInput = input(" > ")
            coordinateTransform = transformInputCoordinate(coordinateInput)
            
            for coordinate in coordinateTransform :
                self.grille[coordinate[0]][coordinate[1]] = "-"
            #
            #
            # NOTE : Maintenant, tu as réusis à créer la grille et à enregistrer les bateaux dedans, mais il faut créer une deuxième taleau qui seras une tableau t'attaque et faire la validation des coordonnées rentré par le joueur avec les consignes dans le doc word


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