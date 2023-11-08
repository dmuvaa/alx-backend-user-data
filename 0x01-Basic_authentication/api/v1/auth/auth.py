#!/usr/bin/python3

from flask import request
from typing import List, TypeVar

"""create a class"""


class Auth:
    """class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """method that returns False path and excluded paths"""
        return False
    

    def authorization_header(self, request=None) -> str:
        """method for authorization header"""
        if request is None:
            return None
    

    def current_user(self, request=None) -> TypeVar('User'):
        """method that returns none"""