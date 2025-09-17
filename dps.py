from personnage import Personnage

class Dps(Personnage):
    def __init__(self, pseudo):
        super().__init__(pseudo)
        self.vie = 80