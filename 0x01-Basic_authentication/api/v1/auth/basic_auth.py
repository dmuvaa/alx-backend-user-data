#!/usr/bin/env python3

"""import some modules"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar

"""Create a class"""


class BasicAuth(Auth):
    """class that inherits from Auth"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """class that returns base64 of the Authorization Header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        head_array = authorization_header.split(" ")
        if head_array[0] != "Basic":
            return None
        else:
            return head_array[1]
