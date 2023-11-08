#!/usr/bin/env python3

"""import modules"""

from flask import request
from typing import List, TypeVar

"""create a class"""


class Auth:
    """class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """method that returns False path and excluded paths"""
        if path is None:
            return True
        if not excluded_paths:
            return True

        normalized_path = path if path.endswith('/') else path + '/'

        for pattern in excluded_paths:
            if pattern.endswith('/') and pattern == normalized_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """method for authorization header"""
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """method that returns none"""
        return None
