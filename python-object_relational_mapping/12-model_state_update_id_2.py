#!/usr/bin/python3
"""Write a script that changes the name of a State object from the database
 hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":
    """The code will not be executed when imported"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    session = Session(engine)

    # Query the State object with id = 2
    state_to_change = session.query(State).filter(State.id == 2).first()

    # Change the state id=2 in the database
    if state_to_change:
        state_to_change.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
