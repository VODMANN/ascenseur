import Ascenseur
import Porte
import Systeme
import Usager

def test_porte_ouverte():
    systeme = Systeme.Systeme()
    ascenseur = Ascenseur.Ascenseur()
    systeme.ascenseur = ascenseur
    porte0 = Porte.Porte(0)
    porte1 = Porte.Porte(1)
    porte2 = Porte.Porte(2)
    porte3 = Porte.Porte(3)
    porte4 = Porte.Porte(4)
    porte5 = Porte.Porte(5)
    systeme.portes = [porte0, porte1, porte2, porte3, porte4, porte5]
    
    porte1.ouvrir()
    

    user1 = Usager.Usager("paul", 1, "haut", 3)
    user2 = Usager.Usager("jeanne", 3, "bas", 2)
    user3 = Usager.Usager("pierre", 4, "bas", 1)
    user4 = Usager.Usager("ines", 0, "haut", 5)
    
    systeme.appele_ascenseur(user1)
    systeme.appele_ascenseur(user2)
    systeme.appele_ascenseur(user3)
    systeme.appele_ascenseur(user4)
    
    systeme.deplacer_asc()
    
test_porte_ouverte()