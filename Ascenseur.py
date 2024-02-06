from couleur_terminal import *


class Ascenseur:
    def __init__(self):
        self.etage = 0
        self.direction = None
        self.destinations = []
        self.en_mouvement = False

    def get_etage(self):
        return self.etage
    
    def get_direction(self):
        return self.direction
    
    def set_en_mouvement(self,mouvement):
        self.en_mouvement = mouvement
    
    def get_en_mouvement(self):
        return self.en_mouvement

    def choisir_direction(self):
        if self.destinations:
            self.direction = "haut" if self.destinations[0] > self.etage else "bas"
        else:
            self.direction = "haut"

    def monter_descendre_etage(self):
        self.en_mouvement = True
        if self.direction == "haut":
            self.etage += 1
        elif self.direction == "bas":
            self.etage -= 1
        print(BLUE + f"L'ascenseur est à l'étage {self.etage}" + RESET)
            
    def deplacer(self):
        if self.etage in self.destinations:
            self.destinations.remove(self.etage)
            return True
        self.choisir_direction()
        self.monter_descendre_etage()
        if self.etage in self.destinations:
            self.destinations.remove(self.etage)
            return True
        elif not self.destinations:
            self.direction = None
            return False
            
    def ajouter_destination(self, etage):
        self.destinations.append(etage)

    def arret_ascenseur(self):
        print(RED + f"L'ascenseur s'arrête à l'étage {self.etage}" + RESET)
        self.en_mouvement = False
        
    def get_destinations(self):
        return self.destinations
    
    def set_etage(self, etage):
        self.etage = etage