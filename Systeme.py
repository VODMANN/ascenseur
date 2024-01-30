class Systeme:
    def __init__(self):
        self.portes = []
        self.ascenseur = None
        self.usager_dehors = []
        self.usager_interieur = []
        
    def portes_fermees(self):
        for porte in self.portes:
            if porte.ouverte:
                return False
        return True
    
    def distance_usager(self, usager):
        return abs(usager.etage - usager.destination)
    
    def appele_ascenseur(self, usager):
        self.usager_dehors.append(usager)
        self.ascenseur.appels.append(usager.etage)
        self.ascenseur.choisir_direction()

    def ouvrir_porte(self, porte):
        if self.portes_fermees() and self.ascenseur.get_en_mouvement() == False:
            if self.ascenseur.get_etage() == porte.get_etage():
                porte.ouvrir()
                porte.attendre_laps_temps(3)
                porte.fermer()
            else:
                print("L'ascenseur n'est pas à cet étage")
        elif self.ascenseur.en_mouvement:
            print("L'ascenseur est en mouvement")
        else:
            print("Une porte est déjà ouverte")

    def get_porte(self, etage):
        for porte in self.portes:
            if porte.get_etage() == etage:
                return porte
        return None
    
    def etat_porte(self, etage):
        porte = self.get_porte(etage)
        if porte is not None:
            return porte.ouverte
        return None
    
    def get_usager_etage(self, etage):
        usager_etage = []
        for usager in self.usagers:
            if usager.get_etage == etage:
                usager_etage.append(usager)
        return usager_etage
    
    def usager_monter(self, etage):
        usager_etage = self.get_usager_etage(etage)
        for usager in usager_etage:
            usager.rentrer_ascenseur()
            if usager.estou():
                self.usager_interieur.append(usager)
                self.usager_dehors.remove(usager)
