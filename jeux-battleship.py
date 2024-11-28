import os
import dataclasses

os.system("cls") 


# --- Constance : ---
NBRTABLEROW = 6    # Nombre de ligne que la grille doit contenir
NBRTABLECOLUMN = 6  # Nombre de colone que la grille doit contenir
NBRBOATS = 3    # Nombre de bateau que chaque joueur peut posséder au début de la partie


# --- Variable dans le code principale : ---
namePlayer1 = str
namePlayer2 = str 
endGame = bool    # Si à True, alors on quitte le jeux et on ferme le programme
error = False   # Permet de détecter si l'utilisateur a entre de mauvais paramètre, et agir en conséquence
player1Turn = bool  # Permet d'activer en boucle le tour du joueur1, pour lui donner au moins un tour, on lui assigne temporairement True
player2Turn = bool  # Permet d'activer en boucle le tour du joueur2, pour lui donner au moins un tour, on lui assigne temporairement True
winningPlayer = str     # Joueur ayant gagner la partie


# --- Fonction : ---
def transformInputCoordinateBoats(coordinateInput, self) -> list:  
    # Fonction pour reçevoir les coordonnées sous forme "ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee" pour l'initialisaton des postions des bateaux
    # et le retourner en une liste qui contient deux listes qui chacune de ces listes sont des coordonnées "ligne, colonne". 
    # En gros, c'est simplement pour transformer les coordonnées entrées par le joueur en une liste,
    # dont les données sont manipulable. Ex : [[ligne1, colonne1], [ligne2, colonne2]]
    # De plus, il permet de valider si le joueur a bien entré les coordonnées, si ce n'est pas le cas, il retourne "error"

    # Les trois lignes suivantes permet de séparer les valeurs
    coordinateInput = coordinateInput.split(sep=",")
    coordinateInput[0] = coordinateInput[0].split(sep="-")
    coordinateInput[1] = coordinateInput[1].split(sep="-")

    for i, contenueI in enumerate(coordinateInput) :    # Les boucles "for" imbriquées servent simplement en tranformer les chiffres, qui sont en str, en int
        for j, contenuJ in enumerate(contenueI) :
            coordinateInput[i][j] = int(coordinateInput[i][j])

    # Validation des coordonnées : 
    if (coordinateInput[0][0] > (NBRTABLEROW - 1) or coordinateInput[0][1] > (NBRTABLECOLUMN - 1) or 
        coordinateInput[1][0] > (NBRTABLEROW - 1) or coordinateInput[1][0] > (NBRTABLECOLUMN - 1)) :
        print("Une des coordonnées est en dehors des limites de la grille !")
        print("Veuillez recommencer... : ")
        input(" > (Enter) ")
        os.system("cls")
        return "error"  # Retourne "error" pour que le code qui appel la fonction peut agir en conséquence, et donc redemander les coordonnées

    if not ((abs(coordinateInput[0][0] - coordinateInput[1][0]) == 1 and coordinateInput[0][1] == coordinateInput[1][1]) or
        (abs(coordinateInput[0][1] - coordinateInput[1][1]) == 1 and coordinateInput[0][0] == coordinateInput[1][0])) :  
        print("Les coordonnées fournies ne sont pas valides pour un bateau de 2 cases !")
        print("Veuillez recommencer... : ")
        input(" > (Enter) ")
        os.system("cls")
        return "error"  # Retourne "error" pour que le code qui appel la fonction peut agir en conséquence, et donc redemander les coordonnées

    if (self.grille[coordinateInput[0][0]][coordinateInput[0][1]] == "-" or 
        self.grille[coordinateInput[1][0]][coordinateInput[1][1]] == "-") :
        print("Un bateau occupe déjà cette place !")
        print("Veuillez recommencer... : ") 
        input(" > (Enter)") 
        os.system("cls")
        return "error"  # Retourne "error" pour que le code qui appel la fonction peut agir en conséquence, et donc redemander les coordonnées

    return [coordinateInput[0], coordinateInput[1]]

def displayGrid(grid) -> None:     # Fonction pour afficher la grille actuelle du joueur 
    print()
    for row in grid :
        for column in row : 
            print(f"[{column}]", end = "")
        print()
    print()


# --- Création de la classe Joueur : ---
@dataclasses.dataclass 
class Joueur : 
    name : str 
    grille = list     # L'état actuelle de la grille du joueurs
    attackGrid = list   # L'état actuelle du la grille d'attaque du joueurs

    def __post_init__(self) -> None :   # Cette fonction initialise les dimensions du pateau et les coordonnées des bateaux lors de la création d'un object Joueur
        coordinateInput = ""    # Coordonné entre par le joueur sous forme "ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee"
        coordinateTransform = []     # Les coordonnées entrées par le joueur pour un bateau qui a été transformer par la fonction "transformInputCoordinate()" 
                                     # en des coordonnées manipulable (sous forme de tableau imbriquer, Ex : [[ligne1, colonne1], [ligne2, colonne2]])
        self.grille = [NBRTABLECOLUMN * [" "] for i in range(NBRTABLEROW)]      # Créer la grille vide
        self.attackGrid = [NBRTABLECOLUMN * [" "] for i in range(NBRTABLEROW)]  # Créer la grille d'attaque vide

        for i in range(NBRBOATS) : 
            error = True    # Temporairement, juste pour faire au moins une itération de la boucle "while error = True", on met "error" à True, même si aucune erreur a été soulevé
            while error == True : 
                error = False  # Au premier tour de la boucle "while", il est impossible qu'il ait des erreurs

                print(f"{self.name}, voici votre grille : ")
                displayGrid(self.grille)
                print(f"{self.name}, entre la position de ton bateau #{i + 1} : (ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee)")
                coordinateInput = input(" > ")
                print()

                coordinateTransform = transformInputCoordinateBoats(coordinateInput, self)
                if coordinateTransform == "error" :     # S'il y a une erreur, alors on redemande la coordonnées au joueur
                    error = True 
                    continue 
                    
            for coordinate in coordinateTransform :     # Permet d'enregistrer un caractère " - " dans la grille selon les coordonnées entrer, signifiant qu'il un bateau à cette place
                self.grille[coordinate[0]][coordinate[1]] = "-"

        os.system("cls")
        print("Voici votre grille de jeux avec vos bateaux : ")
        displayGrid(self.grille)
        input(" > (Enter) ")
        os.system("cls")
            
            
# --- Création de la classe coordonnee : --- 
@dataclasses.dataclass 
class Coordonnee :  
    # Pour ce qui est des coordonnées des tirs, nous allons faire plus simple que la fontion "transformInputCoordinateBoats"
    joueur : object     # Pour pouvoir récupérer grille d'attaque du joueur
    coordinateInputShoot = str  # Coordonnées entrer par l'utilisateur 
    coordinateTranformShoot = list  # Coordonnées transformer, pour pouvoir les manipuler
    ligne = int 
    colonne = int
    error = False    # Permet au programme d'agir en conséquence si la fonction "__post_init__(self) :" détecte une erreur

    def __post_init__(self) :   # Fonction permettant de demander, transformer et valider les coordonnées entrées par le joueur 
        print(f"Veuillez entrer les coordonnées de votre tir : (ligneTir-colonneTir)")
        self.coordinateInputShoot = input(" > ") 
        print()

        self.coordinateTransformShoot = self.coordinateInputShoot.split(sep="-") 
        self.ligne = int(self.coordinateTransformShoot[0])
        self.colonne = int(self.coordinateTransformShoot[1])

        # Validation des coordonnées : 
        if self.ligne > NBRTABLEROW or self.colonne > NBRTABLECOLUMN :
            print(f"Le tir est en dehors de la grille de jeu")
            print(f"Veuillez recommencer... : ") 
            input(" > (Enter)")
            os.system("cls")
            self.error = True

        if self.joueur.grille[self.ligne][self.colonne] == "X" or self.joueur.grille[self.ligne][self.colonne] == "*" : 
            print(f"Vous avez déjà tiré à cet endroit")
            print(f"Veuillez recommencer... : ")
            input(" > (Enter)")
            os.system("cls")
            self.error = True


# --- Début du jeux :  ---
print("Veuillez entrer le nom du premier joueur : ")
namePlayer1 = input(" > ") 
print("\nVeuillez entrer le nom du deuxième joueur : ")
namePlayer2 = input(" > ")
os.system("cls")
player1 = Joueur(namePlayer1) 
player2 = Joueur(namePlayer2)

endGame = False    # Si à True, alors on quitte le jeux et on ferme le programme
player1Turn = True  # Permet d'activer en boucle le tour du joueur1, pour lui donner au moins un tour, on lui assigne temporairement True
player2Turn = True  # Permet d'activer en boucle le tour du joueur2, pour lui donner au moins un tour, on lui assigne temporairement True

while not endGame == True :    # Boucle principale du jeux

    os.system("cls") 
    while  player1Turn == True : 
        os.system("cls")
        print(f"--- C'est au tout de {player1.name} ---")
        print(f"{player1.name}, voici votre grille : ")
        displayGrid(player1.grille)
        print(f"{player1.name}, voici votre grille d'attaque : ")
        displayGrid(player1.attackGrid)

        temporaryObjectShoot = Coordonnee(player1)
        if temporaryObjectShoot.error == True :  # Si la fonction "__post_init__" de la class "Coordonnee" a détecter une erreur, on recommence le tour du joueur sans modification
            del temporaryObjectShoot    # Si les coordonnées on soulevé une erreur, alors on supprime l'object contenant l'erreur
            player1Turn = True
            continue 

        if player2.grille[temporaryObjectShoot.ligne][temporaryObjectShoot.colonne] == " " :
            player1.attackGrid[temporaryObjectShoot.ligne][temporaryObjectShoot.colonne] = "X"  # Modification de la grille d'attaque du joueur1
            player1Turn = False
        
            os.system("cls")
            print(f"--- C'est au tout de {player1.name} ---")
            print(f"{player1.name}, voici votre grille : ")
            displayGrid(player1.grille)
            print(f"{player1.name}, voici votre grille d'attaque : ")
            displayGrid(player1.attackGrid)
            print("Manqué, dommage... ")
            input(" > (Enter)")
        elif player2.grille[temporaryObjectShoot.ligne][temporaryObjectShoot.colonne] == "-" : 
            player1.attackGrid[temporaryObjectShoot.ligne][temporaryObjectShoot.colonne] = "*"  # Modification de la grille d'attaque du joueur1
            player2.grille[temporaryObjectShoot.ligne][temporaryObjectShoot.colonne] = "X"  # Modification de la grille du joueur adverse (joueur2)
            player1Turn = True

            os.system("cls")
            print(f"--- C'est au tout de {player1.name} ---")
            print(f"{player1.name}, voici votre grille : ")
            displayGrid(player1.grille)
            print(f"{player1.name}, voici votre grille d'attaque : ")
            displayGrid(player1.attackGrid)
            print("Touché, bravo !")
            input(" > (Enter)")
        
        # L'utilisation des coordonnées dans ce tour ne seras plus utilisé ultérieurement
        del temporaryObjectShoot  
    # L'orsque que le player1 à jouer son tour, on veut qu'il puisse jouer encore après le tour du player2
    player1Turn = True


    while  player2Turn == True : 
        os.system("cls")
        print(f"--- C'est au tout de {player2.name} ---")
        print(f"{player2.name}, voici votre grille : ")
        displayGrid(player2.grille)
        print(f"{player2.name}, voici votre grille d'attaque : ")
        displayGrid(player2.attackGrid)

        temporaryObjectShoot = Coordonnee(player2)
        if temporaryObjectShoot.error == True :  # Si la fonction "__post_init__" de la class "Coordonnee" a détecter une erreur, on recommence le tour du joueur sans modification
            del temporaryObjectShoot    # Si les coordonnées on soulevé une erreur, alors on supprime l'object contenant l'erreur
            continue 

        if player2.grille[temporaryObjectShoot.ligne][temporaryObjectShoot.colonne] == " " :
            player2.attackGrid[temporaryObjectShoot.ligne][temporaryObjectShoot.colonne] = "X"  # Modification de la grille d'attaque du joueur1
            player2Turn = False

            os.system("cls")
            print(f"--- C'est au tout de {player2.name} ---")
            print(f"{player2.name}, voici votre grille : ")
            displayGrid(player2.grille)
            print(f"{player2.name}, voici votre grille d'attaque : ")
            displayGrid(player2.attackGrid)
            print("Manqué, dommage... ")
            input(" > (Enter)")

        elif player2.grille[temporaryObjectShoot.ligne][temporaryObjectShoot.colonne] == "-" : 
            player2.attackGrid[temporaryObjectShoot.ligne][temporaryObjectShoot.colonne] = "*"  # Modification de la grille d'attaque du joueur1
            player2.grille[temporaryObjectShoot.ligne][temporaryObjectShoot.colonne] = "X"  # Modification de la grille du joueur adverse (joueur2)
            player2Turn = True

            os.system("cls")
            print(f"--- C'est au tout de {player2.name} ---")
            print(f"{player2.name}, voici votre grille : ")
            displayGrid(player2.grille)
            print(f"{player2.name}, voici votre grille d'attaque : ")
            displayGrid(player2.attackGrid)
            print("Touché, bravo !")
            input(" > (Enter)")
        
        # L'utilisation des coordonnées dans ce tour ne seras plus utilisé ultérieurement
        del temporaryObjectShoot 
    # L'orsque que le player2 à jouer son tour, on veut qu'il puisse jouer encore après le tour du player1
    player2Turn = True 

os.system("cls")
print("----------------")
print("Fin de la partie")
print("----------------\n")
print(f"Le gagnant est {winningPlayer}")