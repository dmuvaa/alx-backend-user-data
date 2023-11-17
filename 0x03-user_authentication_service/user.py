#!/usr/bin/env python3

"""import sqlalchemy modules"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


"""Creates a User Class"""


class User(Base):
    """Class that inherits from Base"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        """Main Self"""
        return f"<User(id='{self.id}', email='{self.email}')>"
