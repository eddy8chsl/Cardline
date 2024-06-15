from __future__ import annotations

# -------------------------------------------------------------------------------------------
# classe Animal
# -------------------------------------------------------------------------------------------

class Animal:
    __nom : str
    __nom_scientifique : str
    __taille : float
    __poids : float
    __longevite : int


    def __init__(self, nom : str, nom_scientifique : str, taille : float, poids : float, longevite : int):
        self.__nom = nom
        self.__nom_scientifique = nom_scientifique
        self.__taille = taille
        self.__poids = poids
        self.__longevite = longevite

    def getNom(self) -> str:
        return self.__nom
    
    def getNomScientifique(self) -> str:
        return self.__nom_scientifique

    def getTaille(self) -> float:
        return self.__taille

    def getPoids(self) -> float:
        return self.__poids

    def getLongevite(self) -> int:
        return self.__longevite

    def __lt__(self, autreAni : Animal):
        return self.getTaille() < autreAni.getTaille()

    def comparer(self, autreAni : Animal):
        return self < autreAni
