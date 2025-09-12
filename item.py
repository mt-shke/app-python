# class Item permet de créer des objets equipable par les personnages leur boostant ainsi les stats
class Item:
    nom : str
    rarete : list = ["classic", "rare", "epique"]
    categorie : list = ["cape", "coiffe", "anneau"]
    durabilite : int
    bonus_attaque : int
    bonus_vitalite : int
    bonus_defense : int
    bonus_endurance : int


    def __init__(self, categorie : str, nom : str, rarete : str, bonus_attaque : int = 0, bonus_vitalite : int = 0, bonus_defense : int = 0, bonus_endurance : int = 0):
        self.nom = nom

        if categorie in self.categorie:
            self.categorie = categorie
        else:
            print(f"La catégorie n'est pas connu l'objet doit être de type : {",".join(self.categorie)}")
        if rarete in self.rarete:
            self.rarete = rarete
        else:
            print(f"La rareté n'est pas connu l'objet doit être de rareté : {",".join(self.categorie)}")

        multiplicateur_valeur : float
        match (self.rarete):
            case "classic":
                multiplicateur_valeur = 1
            case "rare":
                multiplicateur_valeur = 1.5
            case "epique":
                multiplicateur_valeur = 2

        self.bonus_attaque = bonus_attaque * multiplicateur_valeur
        self.bonus_vitalite = bonus_vitalite * multiplicateur_valeur
        self.bonus_defense = bonus_defense * multiplicateur_valeur
        self.bonus_endurance = bonus_endurance * multiplicateur_valeur

    def presentation(self):
        return f"""
_________________________________________

Objet : {self.nom}
Raretée -> {self.rarete}
Bonus attaque -> {self.bonus_attaque}
Bonus vitalité -> {self.bonus_vitalite}
Bonus défense -> {self.bonus_defense}
_________________________________________
        """