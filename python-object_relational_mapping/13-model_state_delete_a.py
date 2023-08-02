#!/usr/bin/python3
"""Module that deletes all State objects with a name
   containing the letter a from the database"""

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

    state_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in state_delete:
        session.delete(state)

    session.commit()

    session.close()
    """Close the session"""
