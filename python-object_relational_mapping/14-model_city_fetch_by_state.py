#!/usr/bin/python3
"""Write a script that lists all State objects
 from the database hbtn_0e_6_usa"""

from sys import argv
from model_city import Base, City
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":
    """The code will not be executed when imported"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(City).order_by(City.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
