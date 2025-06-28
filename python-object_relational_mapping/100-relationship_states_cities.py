#!/usr/bin/env python

import sys
import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_base import Base
from relationship_state import State
from relationship_city import City

def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <username> <password> <database>")
        return

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)

    # Crée les tables (states et cities)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Créer l'État et sa ville
    california = State(name="California")
    california.cities = [City(name="San Francisco")]

    session.add(california)
    session.commit()
    session.close()

if __name__ == "__main__":
    main()

    session.close()

if __name__ == "__main__":
    main()
