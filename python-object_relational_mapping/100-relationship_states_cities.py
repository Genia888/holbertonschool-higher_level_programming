#!/usr/bin/python3
"""Creates California with San Francisco in the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def main():
    """Add a State with one City to the database."""
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <username> <password> <database>")
        return

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    california.cities = [City(name="San Francisco")]

    session.add(california)
    session.commit()
    session.close()

if __name__ == "__main__":
    main()
