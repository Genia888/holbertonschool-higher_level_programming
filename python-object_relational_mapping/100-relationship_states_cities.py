#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <mysql_username> <mysql_password> <database_name>")
        return

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connexion à la base
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)

    # Crée les tables si elles n'existent pas
    Base.metadata.create_all(engine)

    # Démarre la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Création de l'État et de la Ville
    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    # Ajout dans la base
    session.add(california)
    session.commit()

    session.close()

if __name__ == "__main__":
    main()
