#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, ForeignKey, Integer, String

import models
from models.city import City
import os




class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    #cities = relationship("City",  backref="states", cascade="delete")
    
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            citylist = []
            city_dict = models.storage.all(models.city.City)
            for key, value in city_dict.items():
                if value.state_id == self.id:
                    citylist.append(value)
            return citylist
    
    else:
        cities_a = relationship("City", backref="states_a",
                              cascade="all, delete-orphan")
    
    
