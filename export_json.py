import sqlite3
import json

#Connexion à la base
conn = sqlite3.connect("produits.db")
cur = conn.cursor()
cur2 = conn.cursor()
cur3 = conn.cursor()
cur4 = conn.cursor()

# Exécuter une requête

cur.execute("SELECT * FROM produits")
rows = cur.fetchall()

cur2.execute("SELECT categorie, SUM (stock*prix) FROM produits GROUP BY categorie")
valeurMarchande = cur2.fetchall()

cur3.execute("SELECT nom FROM produits WHERE stock = 0")
produitRupture = cur3.fetchall()

cur4.execute("SELECT sum(prix * stock) as valeurTotale FROM produits")
valeurTotale = cur4.fetchall()
# Récupérer les noms de colonnes

colonnes = [desc[0] for desc in cur.description]

#Transformer en dictionnaires

donnees = []
for ligne in rows:
    donnees.append(dict(zip(colonnes,ligne)))

colsMarchande = [desc[0] for desc in cur2.description]
marchand = []
for i in valeurMarchande :
    marchand.append(dict(zip(colsMarchande,i)))

colsRupture = [desc[0] for desc in cur3.description]
rupture = []
for i in produitRupture:
    rupture.append(dict(zip(colsRupture,i)))
    
colsTotal = [desc[0] for desc in cur4.description]
totale = []
totale.append(valeurTotale)

export = {
    "produits": donnees,
    "valeurMarchande":valeurMarchande,
    "produitRupture": produitRupture,
    "valeurTotale": valeurTotale
}


#Exporter en JSON
with open("produits_complet.json", "w", encoding="utf-8") as f:
    json.dump(export, f, indent=4, ensure_ascii=False)

print("Export terminé.")

