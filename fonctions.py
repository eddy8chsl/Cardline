# fonctions permettant la manipulation d'une liste d'objets

from typing import List
from animal import Animal
import random


def afficherListe(liste: List[object]) -> None:
    """
    Permet d'afficher le contenu d'une liste
    :param liste: liste d'objets
    """
    for i in range(len(liste)):
        print(str(i) + " - " + str(liste[i].getNom()) + " (" + str(liste[i].getNomScientifique()) + ")")
    print("")

def getElemPrecedent(liste: List[object],pos: int) -> object:
    """
    Retourne l'element précédent la position donnée. None s'il n'existe pas (début de liste)
    :param liste: liste d'objets
    :param pos: position
    """
    prec = None
    if pos > 0:
        prec = liste[pos - 1]
    return prec


def getElemSuivant(liste: List[object], pos: int) -> object:
    """
    Retourne l'élement suivant la position donnée. None s'il n'existe pas (fin de liste)
    :param liste: liste d'objets
    :param pos : entier
    """
    suiv = None
    if pos <= len(liste) - 1:
        suiv = liste[pos]
    return suiv


def getElemInListeAleatoire(liste: List[object]) -> object:
    """
    Renvoie un element tiré au sort dans la liste passée en paramètre
    :param liste: liste d'objets
    :rtype: object
    """
    elem = liste[random.randint(0, len(liste) - 1)]
    return elem

def affichePanel(Cardline : List[object]) -> object:
    print("--------- Cardline ---------")
    for i in range(len(Cardline)):
        print(i, " - ", Cardline[i].getNom())
    print("----------------------------")
