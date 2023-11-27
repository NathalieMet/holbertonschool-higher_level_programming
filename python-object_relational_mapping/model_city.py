#!/usr/bin/python3
"""Write a Python file similar to model_state.py named model_city.py that
 contains the class definition of a City."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """State class that links to the MySQL table 'states'."""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states_id'), nullable=False)
