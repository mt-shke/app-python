from personnage import Personnage
from tank import Tank
from item import Item
from cape import Cape
from coiffe import Coiffe
from menu import choix_personnage

# Suite :
# -> Docstring pour chaque classe (sur la classe et ses méthodes)
# -> Menu CLI pour le choix de l'équipements et du personnage
#   -> Enregistrement dans un fichier JSON pour l'équipements
#   -> Ajouter un systeme d'xp gagner par combat gagné


# Items
cape_de_fou = Item("cape", "cape de fou furieux", "classic", 10, 10, 4, 8)
coiffe_de_fou = Item("coiffe", "coiffe de fou furieux", "rare", 6, 6, 4, 8)
anneau_de_fou = Item("anneau", "anneau de fou furieux", "epique", 4, 4, 2, 8)
stuff = {"cape" : cape_de_fou, "coiffe" : coiffe_de_fou, "anneau" : anneau_de_fou}


# Personnages
p1 = Personnage("Jean Neymar")
# p2 = Personnage("Jean NeyPaMar", stuff)
p3 = Tank("Hubert")

# CLI

print(f"""

*** MENU MINI JEU ***
      
1 : Gestion personnage
        1.a : Renommer le personnage
        1.b : Gestion des caractéristique (+1 points par niveau)
        1.c : Equipements du perso
2 : Gestion Equipements
        2.a : Ajouter un équipement
        2.b : Modifier un équipement
        2.c : Supprimer un équipement
3 : Gestion du jeu
        3.a : Regles du jeu
0 : Quitter le jeu
""")

choix_personnage(p1, p3)

