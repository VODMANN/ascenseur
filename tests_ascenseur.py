import Ascenseur

def test_initialisation(self):
    ascenseur = Ascenseur()
    self.assertEqual(ascenseur.get_etage(), 0)
    self.assertIsNone(ascenseur.get_direction())
    self.assertFalse(ascenseur.get_en_mouvement())
    self.assertEqual(ascenseur.get_destinations(), [])

def test_ajouter_destination(self):
    ascenseur = Ascenseur()
    ascenseur.ajouter_destination(5)
    self.assertEqual(ascenseur.get_destinations(), [5])

def test_choisir_direction(self):
    ascenseur = Ascenseur()
    ascenseur.ajouter_destination(5)
    ascenseur.choisir_direction()
    self.assertEqual(ascenseur.get_direction(), "haut")

def test_monter_descendre_etage(self):
    ascenseur = Ascenseur()
    ascenseur.monter_descendre_etage()
    self.assertEqual(ascenseur.get_etage(), 1)

def test_deplacer(self):
    ascenseur = Ascenseur()
    ascenseur.ajouter_destination(5)
    self.assertTrue(ascenseur.deplacer())
    self.assertEqual(ascenseur.get_etage(), 1)

def test_arret_ascenseur(self):
    ascenseur = Ascenseur()
    ascenseur.arret_ascenseur()
    self.assertFalse(ascenseur.get_en_mouvement())