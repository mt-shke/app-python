from personnage import Personnage

class Tank(Personnage):
    def __init__(self, pseudo):
        super().__init__(pseudo)
        self.vie = 150