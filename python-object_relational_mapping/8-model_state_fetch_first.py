#!/usr/bin/python3
"""Module that lists all State objects from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3],
                                  pool_pre_ping=True))
    """Creating a connection to the MySQL server"""

    Session = sessionmaker(bind=engine)
    """Creating a session to interact with the database"""
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    """Display the result"""
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print('Nothing')

    session.close()
    """Close the session"""
