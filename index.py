import numpy as np
import random as rd

bateaux4_1 = {"longueur":4,"sens":rd.randrange(0,2)}
bateaux3_1_1 = {"longueur":3,"sens":rd.randrange(0,2)}
bateaux3_1_2 = {"longueur":3,"sens":rd.randrange(0,2)}
bateaux2_1_1 = {"longueur":2,"sens":rd.randrange(0,2)}
bateaux2_1_2 = {"longueur":2,"sens":rd.randrange(0,2)}

grille_player=np.arange(16*16).reshape(16,16)
grille_bot=np.arange(16*16).reshape(16,16)

for ligne in range(16):
    for cologne in range (16):
        grille_bot[ligne][cologne]=0
        grille_player[ligne][cologne]=0

def bateauxPositionbot(bateaux,grille):
    bateaux.update({"x": rd.randrange(1,17),"y":rd.randrange(1,17)})
    if bateaux[sens]==0:
        long = bateaux[longueur]
        y = bateaux.y
        for i in range(long):
            grille[y][long].append(1)
            long = long-1
            if long<1:
                for i in range(long):
                    grille[y][long].append(1)
                    long = long+1

    if bateaux[sens]==1:
        long = bateaux[longueur]
        x = bateaux.x
        for i in range(long):
            grille[long][x].append(1)
            long = long-1
            if long<1:
                for i in range(long):
                    grille[long][x].append(1)
                    long = long+1
    return grille



print(bateauxPositionbot(bateaux4_1,grille_bot))




# Etape 1 : Généré une matrice rempli de 0 /
# Etape 2 : Généré les Différents Bateaux qui sont des liste qui contienne plusieur donnée comme leur sens, leur taille ect..
# Etape 3 : Vérifier si le bateau est vertical ou horizontal en créant une fonction is_vert
# Etape 4 : Générer les coordonnés au hasard pour les bateaux.
# Etape 5 : Changer les valeurs des position des bateaux en 1
# Etape 6 : Colorier ses cases qui ont pour valeur 1 en noir
# Etape 7 : Créer une nouvelle matrice 
# Etape 8 : Généré les Différents Bateaux qui sont des liste qui contienne plusieur donnée comme leur sens, leur taille ect..
# Etape 9 : Vérifier si le bateau est vertical ou horizontal en créant une fonction is_vert
# Etape 10 : Générer les coordonnés au hasard pour les bateaux.
# Etape 11 : Changer les valeurs des position des bateaux en 1
# Etape 12 : On va demander a chaque tour une coordonnés au joueur adverse
# Etape 13 : On vérifie si la position est égal à 1 si oui alors la case sera Colorier en rouge  
# Etape 14 : on créra un variable qui rajoutera 1 a chaque fois que une case sera trouver et si elle est égal a 14