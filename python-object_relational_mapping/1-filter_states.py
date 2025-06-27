#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
where the name starts with N.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)

    # Create a cursor to execute queries
    cur = db.cursor()

    # Execute the SQL query to select states starting with "N"
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print all results
    for row in cur.fetchall():
        print(row)

    # Clean up
    cur.close()
    db.close()
