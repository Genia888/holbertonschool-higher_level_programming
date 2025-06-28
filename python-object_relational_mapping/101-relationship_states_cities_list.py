#!/usr/bin/python3
"""Lists all State objects and their City objects from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import State
from relationship_city import City  # Just to ensure model is loaded


def main():
    """List all states and their cities using a relationship."""
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <username> <password> <database>")
        return

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # One single query using joinedload to eagerly load related cities
    states = session.query(State).options(
        joinedload(State.cities)).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda c: c.id):
            print(f"\t{city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    main()
