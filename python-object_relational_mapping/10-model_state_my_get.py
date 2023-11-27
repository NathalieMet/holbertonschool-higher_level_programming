#!/usr/bin/python3
"""Write a script that prints the first State object from the database
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
    state_name_to_search = argv[4]
    state = session.query(State).filter(State.name
                                        == state_name_to_search).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
