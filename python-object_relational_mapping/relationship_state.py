#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Classe State liée à la table states avec une relation vers City."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # Création de la relation avec cascade
    cities = relationship("City", back_populates="state", cascade="all, delete, delete-orphan")
