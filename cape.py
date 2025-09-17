from item import Item

class Cape(Item):
     def __init__(self, categorie, nom):
        super().__init__( categorie, nom)
        self.nom = nom
        self.categorie = categorie