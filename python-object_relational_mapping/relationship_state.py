#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_base import Base

class State(Base):
    """Class that defines a State with a relationship to City"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state", cascade="all, delete, delete-orphan")
