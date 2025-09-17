from item import Item

class Coiffe(Item):
     def __init__(self, categorie, nom):
        super().__init__( categorie, nom)
        self.nom = nom
        self.categorie = categorie