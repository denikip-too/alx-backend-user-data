#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
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
        """returns a User object.
        The method should save the user to the database"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """returns the first row found in the users table"""
        if not kwargs:
            raise NoResultFound
        keys = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in keys:
                raise InvalidRequestError
        res = self._session.query(User).filter_by(**kwargs).one()
        if res is None:
            raise NoResultFound
        self._session.commit()
        return res

    def update_user(self, user_id: int, **kwargs) -> None:
        """takes as argument a required user_id integer
        and arbitrary keyword arguments and return None"""
        if not kwargs:
            raise ValueError
        keys = User.__table__.columns.keys()
        user = self.find_user_by()
        for key, value in user:
            if key not in keys:
                raise ValueError
        res = self._session.query(user).update(**kwargs)
        self._session.commit()
        return res
