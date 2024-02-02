import time
from couleur_terminal import *

class Porte:
    def __init__(self, etage):
        self.etage = etage
        self.ouverte = False

    def ouvrir(self):
        self.ouverte = True
        print(CYAN + f"La porte s'ouvre à l'étage {self.etage}" + RESET)

    def attendre_laps_temps(self, laps_temps):
        time.sleep(laps_temps)

    def get_etage(self):
        return self.etage
    
    def get_ouverte(self):
        return self.ouverte

    def fermer(self):
        self.ouverte = False
        print(ORANGE + f"La porte se ferme à l'étage {self.etage}" + RESET)

