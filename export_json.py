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

cur.execute("SELECT nom FROM produits WHERE stock = 0")
produitRupture = cur.fetchall()

cur.execute("SELECT sum(prix * stock) as valeurTotale FROM produits")
valeurTotale = cur.fetchall()
# Récupérer les noms de colonnes

colonnes = [desc[0] for desc in cur.description]

#Transformer en dictionnaires

donnees = []
for ligne in rows:
    donnees.append(ligne)

marchand = []
for i in valeurMarchande :
    marchand.append(i)

rupture = []
for i in produitRupture:
    rupture.append(i)

totale = []
totale.append(valeurTotale)

export = {
    "produits": rows,
    "valeurMarchande":list(valeurMarchande),
    "produitRupture": list(produitRupture),
    "valeurTotale": valeurTotale
}


#Exporter en JSON
with open("export_complet.json", "w", encoding="utf-8") as f:
    json.dump(export, f, indent=4, ensure_ascii=False)

print("Export terminé.")

