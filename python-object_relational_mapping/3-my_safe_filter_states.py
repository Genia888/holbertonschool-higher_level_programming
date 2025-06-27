#!/usr/bin/python3
"""
Safely lists states that match the given name,
protecting against SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    # Création du curseur
    cur = db.cursor()

    # Requête paramétrée (protection contre injection SQL)
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture
    cur.close()
    db.close()
