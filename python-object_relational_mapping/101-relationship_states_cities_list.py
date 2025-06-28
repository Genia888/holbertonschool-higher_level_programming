#!/usr/bin/python3
"""Lists all State objects and their City objects from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import State
from relationship_city import City  # Just to ensure model is loaded


def main():
    """List all states and their cities using a relationship."""
    # Check if proper arguments are passed
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py"
              "< username > <password > <database >")
        return

    # Retrieve arguments from command line
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine and establish connection to the database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Execute a query that loads all states and their associated cities
    states = session.query(State).options(
        joinedload(State.cities)).order_by(State.id).all()

    # Display each state and its associated cities
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda c: c.id):
            print(f"\t{city.id}: {city.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Ensure the main function runs when this script is executed directly
    main()
