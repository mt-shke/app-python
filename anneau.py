from item import Item

class Anneau(Item):
   def __init__(self, categorie, nom, rarete, bonus_attaque = 0, bonus_vitalite = 0, bonus_defense = 0, bonus_endurance = 0):
      super().__init__(categorie, nom, rarete, bonus_attaque, bonus_vitalite, bonus_defense, bonus_endurance)