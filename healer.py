from personnage import Personnage

class Healer(Personnage):
    def __init__(self, pseudo):
        super().__init__(pseudo)
        self.vie = 120