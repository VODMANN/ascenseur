import Ascenseur
import Porte
import Systeme
import Usager

def main():
    ascenseur = Ascenseur.Ascenseur()
    usager1 = Usager.Usager(0, "haut", 5)
    usager2 = Usager.Usager(0, "haut", 3)
    systeme = Systeme.Systeme()
    systeme.ascenseur = ascenseur
    systeme.portes = {Porte.Porte(0), Porte.Porte(1), Porte.Porte(2), Porte.Porte(3), Porte.Porte(4), Porte.Porte(5)}
    
    