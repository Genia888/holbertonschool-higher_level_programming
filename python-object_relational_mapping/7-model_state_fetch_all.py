#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>")
        return

    # Collect arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine that connects to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}', pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states, sorted by 'id'
    states = session.query(State).order_by(State.id).all()

    # Print results in the requested format
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == '__main__':
    main()
