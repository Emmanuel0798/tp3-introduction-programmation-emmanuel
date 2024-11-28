import os
import dataclasses

os.system("cls") 


# --- Constance : ---
NBRTABLEROW = 6    # Nombre de ligne que la grille doit contenir
NBRTABLECOLUMN = 6  # Nombre de colone que la grille doit contenir
NBRBOATS = 3    # Nombre de bateau que chaque joueur peut posséder au début de la partie


# --- Variable dans le code principale : ---
namePlayer1 = ""
namePlayer2 = "" 
quit = False    # Si à True, alors on quitte le jeux et on ferme le programme
error = False   # Permet de détecter si l'utilisateur a entre de mauvais paramètre, et agir en conséquence


# --- Fonction : ---
def transformInputCoordinate(choice, coordinateInput, self) -> list:  
    # Fonction pour reçevoir les coordonnées sous forme "ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee" et le retourner en une liste qui contient deux listes
    # qui chacune de ces listes sont des coordonnées "ligne, colonne". En gros, c'est simplement pour transformer les coordonnées entrées par le joueur en une liste,
    # dont les données sont manipulable. Ex : [[ligne1, colonne1], [ligne2, colonne2]]
    # De plus, il permet de valider si le joueur a bien entré les coordonnées, si ce n'est pas le cas, il retourne "error"

    if choice == "setBoats" :   # Si la fonction appelée doit renvoyer les coordonnées lors du choix des postions des bateaux
        # Les trois lignes suivantes permet de séparer les valeurs
        coordinateInput = coordinateInput.split(sep=",")
        coordinateInput[0] = coordinateInput[0].split(sep="-")
        coordinateInput[1] = coordinateInput[1].split(sep="-")

        for i, contenueI in enumerate(coordinateInput) :    # Les boucles "for" imbriquées servent simplement en tranformer les chiffres, qui sont en str, en int
            for j, contenuJ in enumerate(contenueI) :
                coordinateInput[i][j] = int(coordinateInput[i][j])

        # Validation des coordonnées : 
        if coordinateInput[0][0] > (NBRTABLEROW - 1) or coordinateInput[0][1] > (NBRTABLECOLUMN - 1) or coordinateInput[1][0] > (NBRTABLEROW - 1) or coordinateInput[1][0] > (NBRTABLECOLUMN - 1) :
            print("Une des coordonnées est en dehors des limites de la grille !")
            print("Veuillez recommencer... : ")
            input(" > (Enter) ")
            return "error"  # Retourne "error" pour que le code qui appel la fonction peut agir en conséquence, et donc redemander les coordonnées

        if not ((abs(coordinateInput[0][0] - coordinateInput[1][0]) == 1 and coordinateInput[0][1] == coordinateInput[1][1]) or
            (abs(coordinateInput[0][1] - coordinateInput[1][1]) == 1 and coordinateInput[0][0] == coordinateInput[1][0])) :  
            print("Les coordonnées fournies ne sont pas valides pour un bateau de 2 cases !")
            print("Veuillez recommencer... : ")
            input(" > (Enter) ")
            return "error"  # Retourne "error" pour que le code qui appel la fonction peut agir en conséquence, et donc redemander les coordonnées

        if (self.grille[coordinateInput[0][0]][coordinateInput[0][1]] == "-" or 
            self.grille[coordinateInput[1][0]][coordinateInput[1][1]] == "-") :
            print("Un bateau occupe déjà cette place !")
            print("Veuillez recommencer... : ") 
            input(" > (Enter)") 
            return "error"  # Retourne "error" pour que le code qui appel la fonction peut agir en conséquence, et donc redemander les coordonnées

        return [coordinateInput[0], coordinateInput[1]]
    
    if choice == "setShoot" :   # Si la fonction appelée doit renvoyer les coordonnées lors du choix de tire
        any 

def displayGrid(self) -> None:     # Fonction pour afficher la grille actuelle du joueur 
    print()
    for row in self.grille :
        for column in row : 
            print(f"[{column}]", end = "")
        print()
    print()


# --- Création de la classe Joueur : ---
@dataclasses.dataclass 
class Joueur : 
    name : str 
    grille = []     # L'état actuelle du plateau du joueurs

    def __post_init__(self) -> None :   # Cette fonction initialise les dimensions du pateau et les coordonnées des bateaux lors de la création d'un object Joueur
        coordinateInput = ""    # Coordonné entre par le joueur sous forme "ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee"
        coordinateTransform = []     # Les coordonnées entrées par le joueur pour un bateau qui a été transformer par la fonction "transformInputCoordinate()" 
                                     # en des coordonnées manipulable (sous forme de tableau imbriquer, Ex : [[ligne1, colonne1], [ligne2, colonne2]])
        self.grille = [NBRTABLECOLUMN * [" "] for i in range(NBRTABLEROW)]      # Créer la grille vide

        for i in range(NBRBOATS) : 
            error = True    # Temporairement, juste pour faire au moins une itération de la boucle "while error = True", on met "error" à True, même si aucune erreur a été soulevé
            while error == True : 
                error = False  # Au premier tour de la boucle "while", il est impossible qu'il ait des erreurs

                print(f"{self.name}, voici votre grille : ")
                displayGrid(self)
                print(f"{self.name}, entre la position de ton bateau #{i + 1} : (ligneDepart-colonneDepart,ligneArrivee-ColonneArrivee)")
                coordinateInput = input(" > ")
                print()

                coordinateTransform = transformInputCoordinate("setBoats", coordinateInput, self)
                if coordinateTransform == "error" :     # S'il y a une erreur, alors on redemande la coordonnées au joueur
                    error = True 
                    continue 
                    
            for coordinate in coordinateTransform :     # Permet d'enregistrer un caractère " - " dans la grille selon les coordonnées entrer, signifiant qu'il un bateau à cette place
                self.grille[coordinate[0]][coordinate[1]] = "-"

        os.system("cls")
        print("Voici votre grille de jeux avec vos bateaux : ")
        displayGrid(self)
        input(" > (Enter) ")
        os.system("cls")
            
            
# --- Création de la classe coordonnee : --- 
@dataclasses.dataclass 
class Coordonnee :
    


# --- Début du jeux :  ---
print("Veuillez entrer le nom du premier joueur : ")
namePlayer1 = input(" > ") 
print("\nVeuillez entrer le nom du deuxième joueur : ")
namePlayer2 = input(" > ")
os.system("cls")
player1 = Joueur(namePlayer1) 
player2 = Joueur(namePlayer2)

while not quit == True :    # Boucle principale du jeux
   any