#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.place import Place
import os

class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)

    states_a = relationship("State", backref="cities_a")

"""
class City(BaseModel, Base):
    The city class, contains state ID and name 
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete-orphan")

    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        initializes City
        super().__init__(*args, **kwargs)
"""
