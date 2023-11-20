#!/usr/bin/env python3

"""Import Modules"""

from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import bcrypt
import uuid


"""Create a Method"""


def _hash_password(password: str) -> str:
    """Method that takes password string arguments and returns bytes"""
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(bytes, salt)
    return hashed_password


def _generate_uuid():
    """Method that returns a string representation of a new UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Method that Returns a User Object"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email=email,
                                     hashed_password=hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Method that Validates User Credentials"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
