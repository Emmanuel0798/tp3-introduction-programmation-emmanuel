import os
os.system("cls") 


# --- Constance : ---
TABLEROW = 6 
TABLECOLUMN = 6


# --- Variable : ---
namePlayer1 = ""
namePlayer2 = ""
tablePlayer1 = []
tablePlayer2 = []


# --- Début du jeux :  ---
print("Veuillez entrer le nom du premier joueur :")
namePlayer1 = input(" > ") 
print("\nVeuillez entrer le nom du deuxième joueur :") 
namePlayer2 = input(" > ")
os.system("cls") 

# Création des tableaux des joueurs : 
tablePlayer1 = [[0] * TABLECOLUMN for i in range(TABLEROW)]

print(tablePlayer1)