#!/usr/bin/python3
"""Module that prints the State object with the name passed as argument"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3],
                                  pool_pre_ping=True))
    """Creating a connection to the MySQL server"""

    state_name = argv[4]
    """Obtaining the name of the state to be searched from the 
    command-line arguments"""
    
    state_found = False
    """Initializing a boolean variable named "state_found" with False"""

    Session = sessionmaker(bind=engine)
    """Creating a session to interact with the database"""
    session = Session()

    for state in session.query(State).order_by(State.id):
        """Display the results if found states"""
        if state.name == state_name:
            print("{}".format(state.id))
            state_found = True
            break

    if state_found is False:
        """Display the results if not found states"""
        print("Not Found")

    session.close()
    """Close the session"""
