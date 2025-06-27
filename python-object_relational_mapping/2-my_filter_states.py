#!/usr/bin/python3
"""
Lists all states with a name exactly matching the user input.
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
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)

    # Création du curseur
    cur = db.cursor()

    # Construction et exécution de la requête (ATTENTION: injection possible ici !)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Nettoyage
    cur.close()
    db.close()
