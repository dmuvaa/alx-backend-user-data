#!/usr/bin/env python3

"""Import a Module"""

from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User

"""Create a Class"""


class SessionAuth(Auth):
    """Empty Class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """method that creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Method that returns a User ID based on a Session ID"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        """Method that returns a User instance based on a cookie value"""
        session_id = self.session_cookie(request)
        if not session_id:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return None
        return User.get(user_id)
