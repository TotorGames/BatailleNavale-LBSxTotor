import numpy as np
import random as rd

bateaux4_1 = {'longueur':4,'sens':rd.randrange(0,2)}
bateaux3_1_1 = {'longueur':3,'sens':rd.randrange(0,2)}
bateaux3_1_2 = {'longueur':3,'sens':rd.randrange(0,2)}
bateaux2_1_1 = {'longueur':2,'sens':rd.randrange(0,2)}
bateaux2_1_2 = {'longueur':2,'sens':rd.randrange(0,2)}

grille_player=np.arange(16*16).reshape(16,16)
grille_bot=np.arange(16*16).reshape(16,16)

for ligne in range(16):
    for cologne in range (16):
        grille_bot[ligne][cologne]=0
        grille_player[ligne][cologne]=0

def bateauxPositionbot(bateaux1,bateaux2,bateaux3,bateaux4,bateaux5,grille):
    bateaux1.update({"x": rd.randrange(1,17),"y":rd.randrange(0,16)})
    bateaux2.update({"x": rd.randrange(1,17),"y":rd.randrange(0,16)})
    bateaux3.update({"x": rd.randrange(1,17),"y":rd.randrange(0,16)})
    bateaux4.update({"x": rd.randrange(1,17),"y":rd.randrange(0,16)})
    bateaux5.update({"x": rd.randrange(1,17),"y":rd.randrange(0,16)})

    #Bateau 1
    if bateaux1['sens']==0:
        long = bateaux1['longueur']
        y = bateaux1['y']
        for i in range(long):
            grille[y][long]=1
            long = long-1
            if long<0:
                for i in range(long):
                    grille[y][long]=1
                    long = long+1
    if bateaux1['sens']==1:
        long = bateaux1['longueur']
        x = bateaux1['x']
        for i in range(long):
            grille[long][x]=1
            long = long-1
            if long<0:
                for i in range(long):
                    grille[long][x] = 1
                    long = long+1
    #_______________________________________#
    #Bateaux 2
    if bateaux2['sens']==0:
        long = bateaux2['longueur']
        y = bateaux2['y']
        for i in range(long):
            grille[y][long]=1
            long = long-1
            if long<0:
                for i in range(long):
                    grille[y][long]=1
                    long = long+1
    if bateaux2['sens']==1:
        long = bateaux2['longueur']
        x = bateaux2['x']
        for i in range(long):
            grille[long][x]=1
            long = long-1
            if long<0:
                for i in range(long):
                    grille[long][x] = 1
                    long = long+1
    #_______________________________________#
    #Bateaux 3
    if bateaux3['sens']==0:
        long = bateaux3['longueur']
        y = bateaux3['y']
        for i in range(long):
            grille[y][long]=1
            long = long-1
            if long<0:
                for i in range(long):
                    grille[y][long]=1
                    long = long+1
    if bateaux3['sens']==1:
        long = bateaux3['longueur']
        x = bateaux3['x']
        for i in range(long):
            grille[long][x]=1
            long = long-1
            if long<0:
                for i in range(long):
                    grille[long][x] = 1
                    long = long+1
    #_______________________________________#
    #Bateaux 4
    if bateaux4['sens']==0:
        long = bateaux4['longueur']
        y = bateaux4['y']
        for i in range(long):
            grille[y][long]=1
            long = long-1
            if long<0:
                for i in range(long):
                    grille[y][long]=1
                    long = long+1
    if bateaux4['sens']==1:
        long = bateaux4['longueur']
        x = bateaux4['x']
        for i in range(long):
            grille[long][x]=1
            long = long-1
            if long<0:
                for i in range(long):
                    grille[long][x] = 1
                    long = long+1
    #_______________________________________#
    #Bateaux 5
    if bateaux5['sens']==0:
        long = bateaux5['longueur']
        y = bateaux5['y']
        for i in range(long):
            grille[y][long]=1
            long = long-1
            if long<0:
                for i in range(long):
                    grille[y][long]=1
                    long = long+1
    if bateaux5['sens']==1:
        long = bateaux5['longueur']
        x = bateaux5['x']
        for i in range(long):
            grille[long][x]=1
            long = long-1
            if long<0:
                for i in range(long):
                    grille[long][x] = 1
                    long = long+1
    return grille


print(bateauxPositionbot(bateaux4_1,bateaux3_1_1,bateaux3_1_2,bateaux2_1_1,bateaux2_1_2,grille_bot))




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