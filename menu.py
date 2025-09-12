import os
from item import Item
from personnage import Personnage
from combat import Combat
import random

FICHIER_JSON = "personnages.json"

# with open(FICHIER_JSON, 'r', encoding='utf-8') as f:
#     data = json.load(f)

# personnages = [Personnage.from_dict(obj) for obj in data]

# for p in personnages:
#     print(p.nom)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nAppuyez sur Entrée pour continuer...")

# --- Sous-menus ---

def menu_gestion_personnage(personnage):
    while True:
        clear()
        print("=== GESTION PERSONNAGE ===")
        print("1.a : Renommer le personnage")
        print("1.b : Gérer les caractéristiques (+1 point par niveau)")
        print("1.c : Voir équipements du perso")
        print("0 : Retour")
        choix = input("\nChoix : ").strip().lower()
        
        if choix == '1.a':
            personnage.renommer(input("Saisir le nouveau pseudo "))
        elif choix == '1.b':
            print("Caractéristiques +1 par niveau (fonction à implémenter)")
            print(personnage.presentation())
        elif choix == '1.c':
            # for ind,inv in personnage.inventaire.items():
            #     print(inv.nom)
            print(personnage.presentation())
        elif choix == '0':
            break
        else:
            print("Choix invalide.")
        pause()


def menu_gestion_equipements(personnage):
    while True:
        clear()
        print("=== GESTION ÉQUIPEMENTS ===")
        print("2.a : Ajouter un équipement")
        print("2.b : Modifier un équipement")
        print("2.c : Supprimer un équipement")
        print("0 : Retour")
        choix = input("\nChoix : ").strip().lower()
        
        if choix == '2.a':
            categorie = input("Saisir une categorie ")
            item = Item("anneau", input("Saisir le nom de l'équipement "), "classic", (random.randint(0, 20), random.randint(0, 30), random.randint(0, 10), random.randint(0, 10)))
            personnage.equipper(categorie, item)
        elif choix == '2.b':
            print("Modifier un équipement (fonction à implémenter)")
        elif choix == '2.c':
            item = input("Saissir l'équipement à supprimer ")
            personnage.supprimer_equipement(item)
        elif choix == '0':
            break
        else:
            print("Choix invalide.")
        pause()


def menu_gestion_jeu():
    while True:
        clear()
        print("=== GESTION DU JEU ===")
        print("3.a : Règles du jeu")
        print("0 : Retour")
        choix = input("\nChoix : ").strip().lower()

        if choix == '3.a':
            print("Voici les règles du jeu (à rédiger)")
        elif choix == '0':
            break
        else:
            print("Choix invalide.")
        pause()

# --- Menu principal ---

def menu_principal(personnage):
    while True:
        clear()
        print("=== MENU PRINCIPAL ===")
        print("1 : Gestion personnage")
        print("2 : Gestion équipements")
        print("3 : Gestion du jeu")
        print("0 : Quitter")
        choix = input("\nChoix : ").strip()
        
        if choix == '1':
            menu_gestion_personnage(personnage)
        elif choix == '2':
            menu_gestion_equipements(personnage)
        elif choix == '3':
            menu_gestion_jeu()
        elif choix == '0':
            print("Fermeture du jeu. À bientôt !")
            break
        else:
            print("Choix invalide.")
            pause()




def choix_personnage(p1, p2):
    while True:
        print("1 : Choisir p1")
        print("2 : Choisir p2")
        print("3 : Demarrer le combat")
        print("0 : Quitter")
        choix = input("\nChoix : ").strip()
        if choix == "1":
            menu_principal(p1)
        
        if choix == "2":
            menu_principal(p2)

        if choix == "3":
            combat = Combat(p1, p2)
            combat.demarrer()
        elif choix == '0':
            break
        else:
            print("Choix invalide.")
            pause()

# if __name__ == "__main__":
#     menu_principal()
