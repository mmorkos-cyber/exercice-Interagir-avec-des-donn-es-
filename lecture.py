import sqlite3
conn = sqlite3.connect("produits.db")
cur = conn.cursor()
cur.execute("SELECT * FROM produits")
rows = cur.fetchall()
for r in rows:
    print(r)
print("-------------------------------------")   
colonnes = [desc[0] for desc in cur.description]
resultat = []
for ligne in rows:
    resultat.append(dict(zip(colonnes, ligne)))
print(resultat)