#!/usr/bin/env python3

"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Method that add user to the database"""
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """method that uses filters to return Users"""
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound("Found no Result")
            return user
        except NoResultFound:
            raise NoResultFound("Found no Result")
        except InvalidRequestError:
            raise InvalidRequestError("request invalid")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Method that updates users in Database"""
        user = self.find_user_by(id=user_id)
        if not User:
            raise ValueError
        valid_keys = ['email', 'hashed_password']
        for key, value in kwargs.items():
            if key not in valid_keys:
                raise ValueError
            setattr(user, key, value)
        self.__session.commit()
        pass
