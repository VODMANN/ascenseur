class Ascenseur:
    def __init__(self):
        self.etage = 0
        self.direction = None
        self.destinations = []
        self.appels = []
        self.en_mouvement = False

    def get_etage(self):
        return self.etage
    
    def get_direction(self):
        return self.direction
    
    def get_en_mouvement(self):
        return self.en_mouvement

    def choisir_direction(self):
        if self.direction is not None:
            return

        if self.appels:
            self.direction = "haut" if self.appels[0] > self.etage else "bas"
        elif self.destinations:
            self.direction = "haut" if self.destinations[0] > self.etage else "bas"
        else:
            self.direction = "haut"

    def monter_descendre_etage(self):
        self.en_mouvement = True
        if self.direction == "haut":
            self.etage += 1
        elif self.direction == "bas":
            self.etage -= 1


    def arret_ascenseur(self):
        self.en_mouvement = False

