#!/usr/bin/env python3

"""Import Modules"""

from db import DB
from sqlalchemy.exc import NoResultFound
from typing import TypeVar
from user import User
import bcrypt

"""Create a Method"""


def _hash_password(password: str) -> str:
    """Method that takes password string arguments and returns bytes"""
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(bytes, salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> TypeVar('User'):
        """Method that Returns a User Object"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User <user's email> already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email=email,
                                     hashed_password=hashed_password)
            return user
