import mysql.connector

# Connexion à la base de données
connexion = mysql.connector.connect(
    host="localhost",        # ou l'IP du serveur MySQL
    user="root",             # ou ton nom d'utilisateur MySQL
    password="",   # ton mot de passe MySQL
    database="ma_premiere_bdd"       # nom de ta base
)

# Création d'un curseur pour exécuter des requêtes SQL
curseur = connexion.cursor()

# Exécution d’une requête SQL
# curseur.execute("""
#     CREATE TABLE IF NOT EXISTS items (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         nom VARCHAR(50),
#         rarete VARCHAR(30),
#         categorie VARCHAR(30),
#         durabilite INT,
#         bonus_attaque INT,
#         bonus_vitalite INT,
#         bonus_defense INT,
#         bonus_endurance INT
#     )
# """)

# items = [
#     ("Épée rouillée", "Commun", "Arme", 25, 3, 0, 0, 1),
#     ("Armure de cuir", "Commun", "Armure", 40, 0, 5, 3, 0),
#     ("Épée de feu", "Épique", "Arme", 80, 15, 0, 2, 5),
#     ("Bouclier sacré", "Légendaire", "Bouclier", 100, 0, 10, 20, 5),
#     ("Anneau d’endurance", "Rare", "Anneau", 999, 0, 0, 0, 15),
#     ("Grimoire ancien", "Épique", "Accessoire", 30, 8, 10, 5, 10),
# ]

# sql = """
#     INSERT INTO items (nom, rarete, categorie, durabilite,
#                        bonus_attaque, bonus_vitalite,
#                        bonus_defense, bonus_endurance)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
# """

# curseur.executemany(sql, items)
# connexion.commit()
print(f"{curseur.rowcount} items insérés.")

curseur.execute("SELECT * FROM items")
for item in curseur.fetchall():
    print(item)