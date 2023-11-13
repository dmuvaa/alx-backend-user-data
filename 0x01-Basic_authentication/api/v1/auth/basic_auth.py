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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """method that returns the decoded value of a string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            string = base64.b64decode(base64_authorization_header)
            new_string = string.decode('utf-8')
            return new_string
        except BaseException:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """method returns user email and pwd from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        decoded_cred = decoded_base64_authorization_header
        if (decoded_cred and isinstance(decoded_cred, str) and
                ":" in decoded_cred):
            res = decoded_cred.split(":", 1)
            return (res[0], res[1])
        return (None, None)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """method that returns User instance based on email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for u in users:
                if u.is_valid_password(user_pwd):
                    return u
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """method overloads Auth and retrieves User instance for a request"""
        auth_header = self.authorization_header(request)
        b64_auth_header = self.extract_base64_authorization_header(auth_header)
        decoded_b64 = self.decode_base64_authorization_header(b64_auth_header)
        user_email, user_pwd = self.extract_user_credentials(decoded_b64)
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user