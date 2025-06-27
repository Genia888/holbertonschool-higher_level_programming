#!/usr/bin/python3
"""
Defines a State class and a Base instance for SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# This will be used to create tables with Base.metadata.create_all()
Base = declarative_base()

class State(Base):
    """State class that maps to the states table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
