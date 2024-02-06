class Usager:
    def __init__(self, nom, etage, direction, destination):
        self.name = nom
        self.etage = etage
        self.direction = direction
        self.destination = destination
        self.dans_ascenseur = False
        self.distrait = False
        
    def get_nom(self):
        return self.name
        
    def set_etage(self, etage):
        self.etage = etage
        
    def set_direction(self, direction):
        self.direction = direction
    
    def set_destination(self, destination):
        self.destination = destination
        
    def get_etage(self):
        return self.etage
    
    def get_direction(self):
        return self.direction
    
    def get_destination(self):
        return self.destination
        
    def rentrer_ascenseur(self):
        if not self.distrait:
            self.dans_ascenseur = True
            
    def set_distrait(self, distrait):
        self.distrait = distrait
    
    def sortir_ascenseur(self):
        self.dans_ascenseur = False
        
    def est_ou(self):
        return self.dans_ascenseur
    




