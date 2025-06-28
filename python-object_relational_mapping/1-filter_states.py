#!/usr/bin/python3
"""List states starting with 'N' from hbtn_0e_0_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    """Main script entry point."""
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    # Create cursor and execute query
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Display results
    for row in cur.fetchall():
        print(row)

    # Close connection
    cur.close()
    db.close()
