import Ascenseur
import Porte
import Systeme
import Usager

def main():
    systeme = Systeme.Systeme()
    ascenseur = Ascenseur.Ascenseur()
    systeme.ascenseur = ascenseur
    systeme.portes = [Porte.Porte(0), Porte.Porte(1), Porte.Porte(2), Porte.Porte(3), Porte.Porte(4), Porte.Porte(5), Porte.Porte(6), Porte.Porte(7)]
    
    user1 = Usager.Usager("paul", 1, "haut", 3)
    user2 = Usager.Usager("jeanne", 3, "bas", 2)
    user3 = Usager.Usager("pierre", 4, "bas", 1)
    user4 = Usager.Usager("ines", 0, "haut", 5)
    user5 = Usager.Usager("marie", 2, "haut", 4)
    user6 = Usager.Usager("lucas", 5, "bas", 0)
    
    systeme.appele_ascenseur(user1)
    systeme.appele_ascenseur(user2)
    systeme.appele_ascenseur(user3)
    systeme.appele_ascenseur(user4)
    systeme.appele_ascenseur(user5)
    systeme.appele_ascenseur(user6)
    
    systeme.deplacer_asc()
    
main()
