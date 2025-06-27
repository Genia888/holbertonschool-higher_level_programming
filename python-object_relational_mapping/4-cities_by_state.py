#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa with their corresponding state.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connexion à la base MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cur = db.cursor()

    # Exécution de la requête (1 seule fois)
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture
    cur.close()
    db.close()
