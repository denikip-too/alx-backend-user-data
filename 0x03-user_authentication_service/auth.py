#!/usr/bin/env python3
"""Hash password"""
import bcrypt
from user import User
from db import DB
import uuid


def _hash_password(password: str) -> bytes:
    """ The returned bytes is a salted hash of the input
    password, hashed with bcrypt.hashpw
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def _generate_uuid() ->str:
    """ return a string representation of a new UUID"""
    random = str(uuid.uuid4())
    return random
