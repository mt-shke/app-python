from item import Item
import json
import os
import uuid

FICHIER_JSON = "personnages.json"

# class Personnage permet de créer des personnages et d'intéragir entre eux
class Personnage:

# Initialise l'instance avec des nouveaux attributs
    def __init__(self, pseudo : str, items = None):
        self.pseudo = pseudo
        self.niveau = 1
        self.id = self.generer_id()
        self.vie = 100
        self.defense = 25
        self.attaque = 25        
        self.endurance = 100
        self.endurance_par_coup = 25
        self.pseudo : str
        self.sous_boost : bool = False
        self.inventaire : dict = {}
        if items != None:
            self.inventaire["cape"] = items["cape"]
            self.inventaire["coiffe"] = items["coiffe"]
            self.inventaire["anneau"] = items["anneau"]
        else:
            print("*****************************************************************************************")
            print(f"*** {self.pseudo} n'as pas d'équipement, il utilise l'équipement par defaut du jeu !  ***") 
            print("*****************************************************************************************")
            self.inventaire = {"cape" : Item("cape", "cape par defaut", "classic", 0, 0, 0, 0),
                         "coiffe" : Item("coiffe", "coiffe par defaut", "classic", 0, 0, 0, 0),
                         "anneau" : Item("anneau", "anneau par defaut", "classic", 0, 0, 0, 0)}
        self.load_stuff()
        self.sauvegarder()

# Attaque une cible et ôte des points de vie
    def attaquer(self, cible):
        if cible.vie <= 0:
            return "perso deja K.O"
        cible.vie = cible.vie - self.attaque
        attaque_booste = self.attaque
        if self.sous_boost:
            self.sous_boost = False
            self.attaque = 25
        return f"{self.pseudo} enleve {round(attaque_booste, 2)} a {cible.pseudo}, il reste {round(cible.vie, 2)} HP a {cible.pseudo}"

# Genere un id unique
    def generer_id(self):
        return str(uuid.uuid4())
 
# Presente le personnage et ses caracteristiques
    def presentation(self):
       info = f"Je suis {self.pseudo}, j'ai {self.vie} points de vie, avec {self.attaque} pour attaque, j'ai une endurance de {self.endurance} et une défense de {self.defense} !\n"
       info += f"Voici mon équipements actuel :"
       for item in self.inventaire.values():
           info += item.presentation()
       return info

# Soigne et remonte les points de vie du personnage
    def soins(self):
        if self.vie == 100:
            return "Votre vie est deja au max !!"
        elif self.vie <= 0:
            return "Personnage deja K.O, impossible de soigner !"
        self.vie = self.vie + self.attaque
        return f"{self.pseudo} vient de se soigner !"

# Booste l'attaque du personnage
    def crier(self):
        attaque_sous_crie = (self.attaque * 0.20) + self.attaque
        # self.attaque *= 1.20 # permet en 1 fois de faire le calcul des 20%
        self.attaque = attaque_sous_crie
        self.sous_boost = True
        return f"{self.pseudo} vient de crier, il attaque maintenant a : {self.attaque}"

# Charge les equipements du personnage et reevalue ses caracteristiques
    def load_stuff(self):
        for item in self.inventaire.values():
            self.attaque += item.bonus_attaque
            self.vie += item.bonus_vitalite
            self.defense += item.bonus_defense
            self.endurance += item.bonus_endurance

# Convertit l'objet personnage pour la sauvegarde en JSON
    def to_dict(self):
        
        items = []
        for n,i in self.inventaire.items():
            items.append({n :i.nom})
        
        return {
            "id": self.id,
            "pseudo": self.pseudo,
            "inventaire": items,
            "niveau": self.niveau,
        }

# Recupere l'objet personnage    
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            nom=data.get("nom"),
            niveau=data.get("niveau")
        )

    # def sauvegarder(self):
    #     data = []
    #     # Charger les données existantes si le fichier existe
    #     if os.path.exists(FICHIER_JSON):
    #         with open(FICHIER_JSON, 'r', encoding='utf-8') as f:
    #             try:
    #                 data = json.load(f)
    #             except json.JSONDecodeError:
    #                 pass  # fichier vide ou invalide
    #     # Ajouter le nouveau personnage

    #     data.append(self.to_dict())
        
    #     # Sauvegarder dans le fichier
    #     with open(FICHIER_JSON, 'w', encoding='utf-8') as f:
    #         json.dump(data, f, indent=4, ensure_ascii=False)

# Sauvegarde le personnage et son inventaire dans le fichier JSON
    def sauvegarder(self):
        data = []
    
        # Charger les données existantes si le fichier existe
        if os.path.exists(FICHIER_JSON):
            with open(FICHIER_JSON, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    pass  # fichier vide ou invalide

        # Convertir l'objet courant en dictionnaire
        obj_dict = self.to_dict()

        # Remplacer l'objet s'il existe déjà (basé sur l'id)
        found = False
        for i, item in enumerate(data):
            if item.get("id") == obj_dict.get("id"):  # ou "nom" si tu n’as pas d’id
                data[i] = obj_dict
                found = True
                break

        # Si non trouvé, l’ajouter
        if not found:
            data.append(obj_dict)

        # Sauvegarder dans le fichier
        with open(FICHIER_JSON, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

# Renomme le personnage
    def renommer(self, nouveau_pseudo):
        ancien_pseudo = self.pseudo
        self.pseudo = nouveau_pseudo  

        # Charger les données existantes
        if os.path.exists(FICHIER_JSON):
            with open(FICHIER_JSON, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

            # Rechercher et modifier le personnage correspondant
            for perso in data:
                if perso.get("pseudo") == ancien_pseudo:
                    perso["pseudo"] = nouveau_pseudo
                    break  # On arrête après avoir trouvé le bon personnage

            # Réécrire le fichier après modification
            with open(FICHIER_JSON, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            print(f"✅ Le pseudo a été changé de '{ancien_pseudo}' à '{nouveau_pseudo}' dans le fichier JSON.")
        
        else:
            print("❌ Fichier JSON introuvable. Aucun changement effectué dans le fichier.")

    def gerer_caracteristiques(self):
        return
    
# Equippe un nouvel item
    def equipper(self, categorie, equipement):
        self.inventaire[categorie] = equipement
        self.sauvegarder()

# Supprime un item de l'inventaire
    def supprimer_equipement(self, nom_item):
        cle_a_supprimer = None
        for cle, item in self.inventaire.items():
            if item.nom == nom_item:
                cle_a_supprimer = cle
                break

        if cle_a_supprimer:
            del self.inventaire[cle_a_supprimer]
            print(f"✅ L'item '{nom_item}' a été supprimé de l'inventaire.")
        else:
            print(f"❌ L'item '{nom_item}' n'existe pas dans l'inventaire.")
            return

        # Mettre à jour le fichier JSON
        if os.path.exists(FICHIER_JSON):
            with open(FICHIER_JSON, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

            # Modifier le bon personnage
            for perso in data:
                if perso.get("pseudo") == self.pseudo:
                    print("Perso actuel: " + self.pseudo)
                    # Supprimer le nom de l'item dans la liste
                    if "inventaire" in perso and nom_item in perso["inventaire"]:
                        perso["inventaire"].remove(nom_item)
                    break

            # Réécriture du fichier JSON
            with open(FICHIER_JSON, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            print(f"✅ L'inventaire de '{self.pseudo}' a été mis à jour dans le fichier JSON.")
        else:
            print("❌ Fichier JSON introuvable. Impossible de mettre à jour l'inventaire.")