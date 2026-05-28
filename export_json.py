import sqlite3
import json
#Connexion à la base
conn = sqlite3.connect("produits.db")
cur = conn.cursor()

# Exécuter une requête

cur.execute("SELECT * FROM produits")
rows = cur.fetchall()
cur.execute("SELECT categorie, SUM (stock*prix) FROM produits GROUP BY categorie")
valeurMarchande = cur.fetchall()

# Récupérer les noms de colonnes

colonnes = [desc[0] for desc in cur.description]

#Transformer en dictionnaires

donnees = []
for ligne in rows:
    donnees.append(ligne)

marchand = []
for i in valeurMarchande :
    marchand.append(i)

#Exporter en JSON

with open("produits.json", "w", encoding="utf-8") as f:
    json.dump(donnees, f, indent=4, ensure_ascii=False)

with open("valeurMarchande.json", "w", encoding="utf-8") as f:
    json.dump (marchand,f,indent=4, ensure_ascii=False)

print("Export terminé.")

