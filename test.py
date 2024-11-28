import os 
import dataclasses
os.system("cls")

error = True    # Temporaire

while error == True :
    print(f"Nouvelle itération de la boucle \"while\", error : {error}")
    error = False 
    choix = input(" > ")
    if choix == "error" : 
        print("Erreur détecté")
        error = True
        continue

print("Fin de la boucle while")