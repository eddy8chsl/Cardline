# Programme s'inspirant du jeu Cardline
__authors__ = "Prof"
__version__ = "1.0.0"
__date__ = "2023/02"

from typing import List
import random

from animal import Animal
from fonctions import afficherListe, getElemPrecedent, getElemSuivant, getElemInListeAleatoire, affichePanel

# -------------------------------------------------------------------------------------------
# fonction d'affichage et de comparaison
# -------------------------------------------------------------------------------------------

def choisirPlace(numMax : int) -> int:
    """Permet de choisir la position pour placer la carte en respectant la taille de la liste.
    :param numMax : valeur max de placement possible
    :return: la position choisie
    """
    # TODO : à implémenter
    pos = int(input("Place ? (Choisissez la place de l'animal qui sera situé juste après ou ajouter 1 à la dernière position pour placer en fin de liste): "))
    if pos > numMax:
        pos = numMax
    return pos
    

def comparer(ani: Animal, autreAni: Animal) -> bool:
    """Compare ani et autreAni selon la taille.
    :param ani : animal à comparer au second
    :param autreAni : animal à comparer
    :return : Renvoie True si la taille d'ani est plus petite ou égale à celle d'autreAni. False sinon"""
    return ani.comparer(autreAni)

def jouerNouvelleCarte() -> str:
    """Permet de proposer de jouer une nouvelle carte O/N
    :return: la réponse : O ou N
    """
    choix = input("Jouer une nouvelle carte : O/N ? ")
    while choix != 'O' and choix != 'N':
        choix = input("Jouer une nouvelle carte : O/N ? ")
    return choix

def menu():
    """
    Affichage du menu et sélection du choix du joueur
    :return:
    """
    print("Menu : ")
    print("1 - afficher la liste des animaux")
    print("2 - jouer à la classification selon la taille ")
    print("3 - ajouter un nouvel animal ")
    print("9 - quitter")
    choix = int(input("Votre Choix ? : "))
    while choix != 1 and choix != 2 and choix != 3 and choix != 9:
        choix = int(input("Votre Choix ? : "))
    return choix

def testerInsertionAnimal(listeAni : List[Animal], pos: int, unAni: Animal)-> bool:
    """Permet de vérifier la position pour l'insertion dans une liste
    :param listeAni: liste des animaux ordonnées selon la taille
    :param pos: place proposée pour insérer
    :param unAni: animal
    :return:
        Renvoie True si place est la bonne position pour insérer unAni dans la liste en respectant le critère de taille. False sinon.
    """
    booleen =  False
    elem_precedent = getElemPrecedent(listeAni, pos)
    elem_suivant = getElemSuivant(listeAni, pos)
    if elem_precedent == None:
        if comparer(unAni, elem_suivant) == True:
            booleen = True
    elif elem_suivant == None:
        if comparer(elem_precedent, unAni) == True:
            booleen = True
    else:
        if comparer(unAni, elem_suivant) == True and comparer(elem_precedent, unAni) == True:
            booleen = True
    return booleen

# ----------------------------------------------------------------------------------------------------------------#
# PROGRAMME PRINCIPAL --------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------#

# création des cartes
listeAnimaux = [Animal("Chat", "chaiuit", 0.3, 8, 14), Animal("Lion", "Panthera leo", 1.75, 120, 14), Animal("Loup Gris", "Canis lupus Linnaeus", 1.3, 38, 10), Animal("Mouton", "Ovis aries", 1.2, 90, 12)]
#TODO ETAPE 1 : création des animaux

#TODO : initialisation de la pioche (mélangée) et de la cardline(une carte de départ)

print("Bienvenue dans le jeu Cardline : le but consiste à ordonnner les animaux selon une caractéristique : la taille")
choix = menu()
while choix != 9:

    if choix == 1:
        afficherListe(listeAnimaux)

    elif choix == 2:
        cp_listeAnimaux = list(listeAnimaux)
        cardline = []
        while jouerNouvelleCarte() != 'N':
            if len(cp_listeAnimaux) != 0:
                if len(cardline) < 1:
                    carte_aleatoire = random.randint(0, len(cp_listeAnimaux)) - 1
                    cardline.append(cp_listeAnimaux[carte_aleatoire])
                    cp_listeAnimaux.pop(carte_aleatoire)

                affichePanel(cardline)
                
                carte_aleatoire = random.randint(0, len(cp_listeAnimaux)) - 1
                animal_placer = cp_listeAnimaux[carte_aleatoire]
                print("Nouvel animal à placer :", animal_placer.getNom())

                pos = choisirPlace(len(cardline))
                if testerInsertionAnimal(cardline, pos, animal_placer) == True:
                    cp_listeAnimaux.pop(carte_aleatoire)
                    cardline.insert(pos, animal_placer)
                    print("Bravo !\n")
                else:
                    print("Perdu :(\n")

                affichePanel(cardline)
                print("")
            else:
                print("\nTout les animaux de la liste sont classifiés, impossible de jouer une nouvelle carte !\n")

        #ETAPE2 - partie Niveau 1 : 1 carte à placer par rapport à une carte de cardline
        #TODO ETAPE 2 : création de la cardline
        #TODO ETAPE 2 : ajout d'une carte aléatoire à la cardline
        #TODO ETAPE 2 : affichage de la cardline
        #TODO ETAPE 2 : proposer une carte Animal à jouer, tirée aléatoirement
        #TODO ETAPE 2 : choix du placement par le joueur dans la cardline
        #TODO ETAPE 2 : vérification de la proposition du joueur et affichage du résultat
        #TODO ETAPE 2 : si OK, ajout à la cardline, sinon defausse de la carte jouée
        #TODO ETAPE 2 : affichage de la cardline

        #ETAPE2 - partie Niveau 2 : le joueur peut jouer plusieurs cartes


    elif choix == 3:
        name_animal = input("Nom de l'animal: ")
        name_scientifique_aninal = input("Nom scientique de l'animal: ")
        taille_animal = float(input("Taille de l'animal (en m): "))
        poids_animal = float(input("Poids de l'animal (en kg): "))
        longevite_animal = int(input("Longévité de l'animal (en année): "))
        print("")
        animal_implenter = Animal(name_animal, name_scientifique_aninal, taille_animal, poids_animal, longevite_animal)
        listeAnimaux.append(animal_implenter)

    choix = menu()

print("Au revoir !")
