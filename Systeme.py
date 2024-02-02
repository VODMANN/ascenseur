from couleur_terminal import *

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
        self.ascenseur.ajouter_destination(usager.etage)

    def ouvrir_porte(self, porte):
        if self.portes_fermees() and self.ascenseur.get_en_mouvement() == False:
            if self.ascenseur.get_etage() == porte.get_etage():
                porte.ouvrir()
                return True
            else:
                print("L'ascenseur n'est pas à cet étage")
                return False
        elif self.ascenseur.en_mouvement:
            print("L'ascenseur est en mouvement")
            return False
        else:
            print("Une porte est déjà ouverte")
            return False
        
    def portes_fermees(self):
        for porte in self.portes:
            if porte.ouverte:
                return False
        return True
            
    def fermer_porte(self, porte):
        if porte.ouverte:
            porte.fermer()
        else:
            print("La porte est déjà fermée")

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
        for usager in self.usager_dehors:
            if usager.get_etage() == etage:
                usager_etage.append(usager)
        return usager_etage
    
    def usager_monter(self, etage):
        usager_etage = self.get_usager_etage(etage)
        for usager in usager_etage:
            etage = False
            for porte in self.portes:
                if porte.get_etage() == usager.get_destination():
                    etage = True
            if etage:
                usager.rentrer_ascenseur()
                if usager.est_ou():
                    self.usager_interieur.append(usager)
                    self.usager_dehors.remove(usager)
                    self.ascenseur.ajouter_destination(usager.get_destination())
                    print(GREEN + "Usager Monté: " + RESET + usager.get_nom() )
                else:
                    print("Usager distrait: " + usager.get_nom())
            else:
                print( RED +"Impossible pour " + usager.get_nom() + " d'aller à l'étage " + str(usager.get_destination()) + RESET)

                
    def usager_descendre(self):
        for usager in self.usager_interieur:
            if usager.get_destination() == self.ascenseur.get_etage():
                usager.sortir_ascenseur()
                self.usager_interieur.remove(usager)
                print(YELLOW + "Usager sorti: " + RESET + usager.get_nom())
                
    def deplacer_asc(self):
        print("Destination: " + str(self.ascenseur.get_destinations()))
        if self.ascenseur.deplacer():
            self.ascenseur.arret_ascenseur()
            if(self.ouvrir_porte(self.get_porte(self.ascenseur.get_etage()))):
                self.usager_descendre()
                self.usager_monter(self.ascenseur.get_etage())
            self.fermer_porte(self.get_porte(self.ascenseur.get_etage()))
        if len(self.ascenseur.get_destinations())>0:
            if(self.portes_fermees()):
                print(VIOLET +  "Ascenseur repart avec" + WHITE + self.get_nom_usager_interieur() + VIOLET + " à bord" + RESET)
                self.deplacer_asc()
            else:
                print("Ascenseur à l'arrêt: portes ouvertes")
        else:
            print("Ascenseur à l'arrêt: plus de destination")

        

    def get_nom_usager_interieur(self):
        noms = ""
        for usager in self.usager_interieur:
            noms += " " + usager.get_nom()
        return noms