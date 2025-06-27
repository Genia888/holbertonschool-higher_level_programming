#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à MySQL
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=dbname)

    cur = db.cursor()

    # Requête sécurisée avec paramètre (protection contre injection)
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id
    """
    cur.execute(query, (state_name,))

    # Affichage des résultats sous forme "ville1, ville2, ville3"
    rows = cur.fetchall()
    print(", ".join([city[0] for city in rows]))

    cur.close()
    db.close()
