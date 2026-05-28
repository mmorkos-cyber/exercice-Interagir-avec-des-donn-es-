import sqlite3
import json

#Connexion à la base
conn = sqlite3.connect("produits.db")
cur = conn.cursor()

# Exécuter une requête
cur.execute("SELECT * FROM produits")
rows = cur.fetchall()

cur.execute("SELECT nom FROM produits WHERE stock = 0")
produitRupture = cur.fetchall()

cur.execute("SELECT sum(prix * stock) as valeurTotale FROM produits")
valeurTotale = cur.fetchall
# Récupérer les noms de colonnes
colonnes = [desc[0] for desc in cur.description]
#Transformer en dictionnaires
donnees = []
for ligne in rows:
    donnees.append(ligne)
#Exporter en JSON
with open("produits.json", "w", encoding="utf-8") as f:
    json.dump(donnees, f, indent=4, ensure_ascii=False)
print("Export terminé.")