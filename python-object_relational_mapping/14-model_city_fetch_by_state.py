#!/usr/bin/python3
"""Module that deletes all State objects with a name
   containing the letter a from the database"""

from sys import argv
from model_state import Base, State
from model_city import City
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

    query_lines = session.query(City, State).\
        filter(City.state_id == State.id).all()
    """Quering and retrieving all City.State objects with
       matching state_id from City and State tables"""

    for city, state in query_lines:
        """Display the results"""
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
    """Close the session"""
