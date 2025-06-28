#!/usr/bin/env python

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_base import Base  # <- Base partagé

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # Utilisation de "City" en tant que string, évite l'import circulaire
    cities = relationship("City", back_populates="state", cascade="all, delete, delete-orphan")
