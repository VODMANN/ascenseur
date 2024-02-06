from Ascenseur import Ascenseur 
from Porte import Porte
from Systeme import Systeme
from Usager import Usager
import unittest


    
class TestUsagerMethods(unittest.TestCase):
    def test_usager_distrait(self):
        systeme = Systeme()
        ascenseur = Ascenseur()
        ascenseur.set_etage(1)
        systeme.ascenseur = ascenseur
        porte0 = Porte(0)
        porte1 = Porte(1)
        porte2 = Porte(2)
        porte3 = Porte(3)
        porte4 = Porte(4)
        porte5 = Porte(5)
        systeme.portes = [porte0, porte1, porte2, porte3, porte4, porte5]
        
        porte1.ouvrir()

        user1 = Usager("paul", 1, "haut", 3)
        user1.set_distrait(True)
        systeme.appele_ascenseur(user1)
        systeme.usager_monter(1)
        
        self.assertEqual(user1.est_ou(), False)
        
    def test_get_nom(self):
        self.usager = Usager("John", 5, "Monte", 10)
        self.assertEqual(self.usager.get_nom(), "John")

    def test_set_etage(self):
        self.usager = Usager("John", 5, "Monte", 10)
        self.usager.set_etage(3)
        self.assertEqual(self.usager.get_etage(), 3)

    def test_set_direction(self):
        self.usager = Usager("John", 5, "Monte", 10)
        self.usager.set_direction("Descend")
        self.assertEqual(self.usager.get_direction(), "Descend")

    def test_set_destination(self):
        self.usager = Usager("John", 5, "Monte", 10)
        self.usager.set_destination(7)
        self.assertEqual(self.usager.get_destination(), 7)

    def test_get_etage(self):
        self.usager = Usager("John", 5, "Monte", 10)
        self.assertEqual(self.usager.get_etage(), 5)

    def test_get_direction(self):
        self.usager = Usager("John", 5, "Monte", 10)
        self.assertEqual(self.usager.get_direction(), "Monte")

    def test_get_destination(self):
        self.usager = Usager("John", 5, "Monte", 10)
        self.assertEqual(self.usager.get_destination(), 10)

    def test_set_distrait(self):
        self.usager = Usager("John", 5, "Monte", 10)
        self.usager.set_distrait(True)
        self.assertTrue(self.usager.distrait)
        
    def test_sortir_ascenseur(self):
        self.usager = Usager("John", 5, "Monte", 10)
        self.usager.sortir_ascenseur()
        self.assertFalse(self.usager.est_ou())
        


class TestAscenseur(unittest.TestCase):
    def setUp(self):
        self.ascenseur = Ascenseur()

    def test_get_etage(self):
        self.assertEqual(self.ascenseur.get_etage(), 0)

    def test_get_direction(self):
        self.assertIsNone(self.ascenseur.get_direction())

    def test_get_en_mouvement(self):
        self.assertFalse(self.ascenseur.get_en_mouvement())

    def test_initialisation(self):
        self.assertEqual(self.ascenseur.etage, 0)
        self.assertIsNone(self.ascenseur.direction)
        self.assertFalse(self.ascenseur.en_mouvement)
        self.assertEqual(self.ascenseur.destinations, [])

    def test_choisir_direction(self):
        self.ascenseur.destinations = [3, 5, 2]
        self.ascenseur.etage = 2
        self.ascenseur.choisir_direction()
        self.assertEqual(self.ascenseur.direction, "haut")

        self.ascenseur.etage = 4
        self.ascenseur.choisir_direction()
        self.assertEqual(self.ascenseur.direction, "bas")

    def test_monter_descendre_etage(self):
        self.ascenseur.direction = "haut"
        self.ascenseur.monter_descendre_etage()
        self.assertEqual(self.ascenseur.etage, 1)

        self.ascenseur.direction = "bas"
        self.ascenseur.monter_descendre_etage()
        self.assertEqual(self.ascenseur.etage, 0)

    def test_deplacer(self):
        self.ascenseur.destinations = [3, 5, 2]
        self.ascenseur.etage = 2
        self.assertTrue(self.ascenseur.deplacer())
        self.assertEqual(self.ascenseur.destinations, [3, 5])

        self.ascenseur.etage = 3
        self.assertTrue(self.ascenseur.deplacer())
        self.assertEqual(self.ascenseur.destinations, [5])

        self.ascenseur.etage = 5
        self.assertTrue(self.ascenseur.deplacer())
        self.assertEqual(self.ascenseur.destinations, [])

        self.assertFalse(self.ascenseur.deplacer())

    def test_ajouter_destination(self):
        self.ascenseur.ajouter_destination(4)
        self.assertEqual(self.ascenseur.destinations, [4])

        self.ascenseur.ajouter_destination(1)
        self.assertEqual(self.ascenseur.destinations, [4, 1])

    def test_arret_ascenseur(self):
        self.ascenseur.arret_ascenseur()
        self.assertFalse(self.ascenseur.en_mouvement)

    def test_get_destinations(self):
        self.assertEqual(self.ascenseur.get_destinations(), [])

        self.ascenseur.destinations = [3, 5]
        self.assertEqual(self.ascenseur.get_destinations(), [3, 5])

    def test_deplacer2(self):
        ascenseur = Ascenseur()
        ascenseur.ajouter_destination(4)
        ascenseur.choisir_direction()
        ascenseur.deplacer()
        self.assertTrue(ascenseur.get_etage() == 1)
        ascenseur.deplacer()
        self.assertTrue(ascenseur.get_etage() == 2)
        ascenseur.deplacer()
        self.assertTrue(ascenseur.get_etage() == 3)
        ascenseur.deplacer()
        self.assertTrue(ascenseur.get_etage() == 4)

    
class TestSystemeMethods(unittest.TestCase):

    def test_distance_usager(self):
        systeme = Systeme()
        usager = Usager("Alice", 3, "haut", 7)
        self.assertEqual(systeme.distance_usager(usager), 4)

    def test_appele_ascenseur(self):
        systeme = Systeme()
        ascenseur = Ascenseur()
        systeme.ascenseur = ascenseur
        usager = Usager("Bob", 2, "bas", 1)
        systeme.appele_ascenseur(usager)
        self.assertIn(usager, systeme.usager_dehors)
        self.assertIn(2, systeme.ascenseur.get_destinations())


    def test_fermer_porte(self):
        systeme = Systeme()
        porte1 = Porte(1)
        systeme.portes = [porte1]
        systeme.fermer_porte(porte1)
        self.assertFalse(porte1.get_ouverte())

    def test_usager_monter(self):
        systeme = Systeme()
        ascenseur = Ascenseur()
        ascenseur.set_etage(1)
        systeme.ascenseur = ascenseur
        porte1 = Porte(1)
        porte2 = Porte(2)
        porte3 = Porte(3)
        systeme.portes = [porte1, porte2, porte3]
        usager = Usager("Charlie", 1, "haut", 3)
        systeme.appele_ascenseur(usager)
        porte1.ouvrir()
        systeme.usager_monter(1)
        self.assertIn(usager, systeme.usager_interieur)
        
    def test_portes_ouvertes(self):
        systeme = Systeme()
        porte1 = Porte(1)
        porte2 = Porte(2)
        systeme.portes = [porte1, porte2]
        porte1.ouvrir()
        self.assertFalse(systeme.portes_fermees())
        
    def test_portes_fermees_portes_vide(self):
        systeme = Systeme()
        self.assertTrue(systeme.portes_fermees())
        
    def test_portes_fermees(self):
        systeme = Systeme()
        porte1 = Porte(1)
        porte2 = Porte(2)
        systeme.portes = [porte1, porte2]
        self.assertTrue(systeme.portes_fermees())
        
    def test_ouvrir_porte(self):
        systeme = Systeme()
        ascenseur = Ascenseur()
        ascenseur.set_etage(1)
        systeme.ascenseur = ascenseur
        porte1 = Porte(1)
        systeme.portes = [porte1]

        self.assertTrue(systeme.ouvrir_porte(porte1))

        porte2 = Porte(2)
        self.assertFalse(systeme.ouvrir_porte(porte2))

        porte1.ouvrir()
        self.assertFalse(systeme.ouvrir_porte(porte1))



    def test_get_nom_usager_interieur(self):
        systeme = Systeme()
        ascenseur = Ascenseur()
        ascenseur.set_etage(1)
        systeme.ascenseur = ascenseur
        porte1 = Porte(1)
        systeme.portes = [porte1]

        usager1 = Usager("Alice", 1, "haut", 3)
        usager2 = Usager("Bob", 1, "bas", 2)
        systeme.usager_interieur = [usager1, usager2]

        self.assertEqual(systeme.get_nom_usager_interieur(), " Alice Bob")
        
    def test_ascenseur_pas_etage(self):
        systeme = Systeme()
        ascenseur = Ascenseur()
        ascenseur.set_etage(1)
        systeme.ascenseur = ascenseur
        porte1 = Porte(1)
        porte2 = Porte(2)
        systeme.portes = [porte1, porte2]
        
        systeme.ouvrir_porte(porte2)
        
    def test_fermer_une_porte(self):
        systeme = Systeme()
        ascenseur = Ascenseur()
        ascenseur.set_etage(1)
        systeme.ascenseur = ascenseur
        porte1 = Porte(1)
        porte2 = Porte(2)
        systeme.portes = [porte1, porte2]
        porte1.ouvrir()
        systeme.fermer_porte(porte1)
    
    def test_ascenseur_en_mouvement(self):
        systeme = Systeme()
        ascenseur = Ascenseur()
        ascenseur.set_etage(1)
        systeme.ascenseur = ascenseur
        ascenseur.set_en_mouvement(True)
        porte1 = Porte(1)
        porte2 = Porte(2)
        systeme.portes = [porte1, porte2]
        
        systeme.ouvrir_porte(porte2)
        
    def test_porte_inexistante(self):
        systeme = Systeme()
        self.assertEqual(systeme.get_porte(1), None)

        
    def test_usager_monter_impossible(self):
        systeme = Systeme()
        ascenseur = Ascenseur()
        ascenseur.set_etage(1)
        systeme.ascenseur = ascenseur
        porte1 = Porte(1)
        porte2 = Porte(2)
        systeme.portes = [porte1, porte2]
        usager = Usager("Charlie", 1, "haut", 3)
        systeme.appele_ascenseur(usager)
        porte1.ouvrir()
        systeme.usager_monter(1)
        
    def test_usager_descendre(self):
        systeme = Systeme()
        ascenseur = Ascenseur()
        ascenseur.set_etage(1)
        systeme.ascenseur = ascenseur
        systeme.ascenseur.set_etage(1)
        porte1 = Porte(1)
        porte2 = Porte(2)
        porte3 = Porte(3)
        systeme.portes = [porte1, porte2, porte3]
        usager = Usager("Charlie", 3, "bas", 1)
        systeme.usager_interieur = [usager]
        systeme.usager_descendre()
        
    def test_deplacer_asc(self):
        systeme = Systeme()
        ascenseur = Ascenseur()
        systeme.ascenseur = ascenseur
        systeme.portes = [Porte(0), Porte(1), Porte(2), Porte(3), Porte(4), Porte(5)]
        

        user1 = Usager("paul", 1, "haut", 3)
        user2 = Usager("jeanne", 3, "bas", 2)
        user3 = Usager("pierre", 4, "bas", 1)
        user4 = Usager("ines", 0, "haut", 5)
        
        systeme.appele_ascenseur(user1)
        systeme.appele_ascenseur(user2)
        systeme.appele_ascenseur(user3)
        systeme.appele_ascenseur(user4)
        
        systeme.deplacer_asc()
        




class TestPorteMethods(unittest.TestCase):

    def test_get_etage(self):
        porte = Porte(2)
        self.assertEqual(porte.get_etage(), 2)

    def test_get_ouverte(self):
        porte = Porte(0)
        porte.ouvrir()
        self.assertTrue(porte.get_ouverte())


    def test_fermer(self):
        porte = Porte(3)
        porte.ouvrir()
        porte.fermer()
        self.assertFalse(porte.get_ouverte())
        
    def test_porte_ouverte(self):
        systeme = Systeme()
        ascenseur = Ascenseur()
        systeme.ascenseur = ascenseur
        porte0 = Porte(0)
        porte1 = Porte(1)
        porte2 = Porte(2)
        porte3 = Porte(3)
        porte4 = Porte(4)
        porte5 = Porte(5)
        systeme.portes = [porte0, porte1, porte2, porte3, porte4, porte5]
        
        porte1.ouvrir()
        

        user1 = Usager("paul", 1, "haut", 3)
        user2 = Usager("jeanne", 3, "bas", 2)
        user3 = Usager("pierre", 4, "bas", 1)
        user4 = Usager("ines", 0, "haut", 5)
        
        systeme.appele_ascenseur(user1)
        systeme.appele_ascenseur(user2)
        systeme.appele_ascenseur(user3)
        systeme.appele_ascenseur(user4)
        
        self.assertEqual(systeme.deplacer_asc(), False)



