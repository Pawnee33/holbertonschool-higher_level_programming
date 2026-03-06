#!/usr/bin/python3
"""
Module that defines the City class and links it to the cities table.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that represents the cities table.
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
