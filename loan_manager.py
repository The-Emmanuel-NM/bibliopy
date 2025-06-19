import sqlite3
#connexion a la base des données
conn = sqlite3.connect("bibliotheque.db")
cursor = conn.cursor()
#création des tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS livres(
 id INTEGER PRIMARY KEY, titre TEXT, auteur TEXT, disponible BOOLEAN )""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS emprunts(
 id INTEGER PRIMARY KEY, utilisateur TEXT, livre_id INTEGER, date_emprunt DATE, date_retour DATE, FOREIGN KEY(livre_id)REFERENCES livres(id))""")
conn.commit()

#fonction pour emprunter un livre
def emprunter_livre(utilisateur,livre_id):
    cursor.execute("SELECT disponible FROM livres WHERE id =?", (livre_id))
    livre= cursor.fetchone()
    if livre and livre[0]:
        cursor.execute("INSERT INTO emprunts(utisateur,livre_id, date_emprunt) VALUES(?,?, DATE('now'))",( utilisateur,livre_id))
        cursor.execute("UPDATE livres SET disponible = 0 WHERE id =?",(livre_id,))
        conn.commit()
        print("livre emprunté avec succès!")
    else:
        print("Le livre n'est pas disponible.")
        
#fonction pour retourner un livre
def retourner_livre(livre_id):
    cursor.execute("UPDATE livres SET disponible = 1 WHERE id = ?",(livre_id,))
    cursor.execute("UPDATE emprunts SET date_retour = DATE('now') WHERE livre_id =? AND date_retour IS NULL",(livre_id,))
    conn.commit()
    print("Livre retourné avec succès!")

#fonction pour filtrer les livres disponibles
def livres_disponibles():
    cursor.execute ("SELECT id,titre,auteur FROM livres WHERE disponible = 1")
    livres = cursor.fetchall()
    for livre in livres:
        print(f"ID:{livre[0]},Titre:{livre[1]},Auteur{livre[2]}")
        

