#!/usr/bin/env python3

"""Import Modules"""

import bcrypt

"""Create a Method"""


def _hash_password(password: str) -> str:
    """Method that takes password string arguments and returns bytes"""
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(bytes, salt)
    return hashed_password
