#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, DateTime, Column, ForeignKey
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class
        Attribute:
               -name: customer name
    """
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """Gettext method in cae of file storage"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
