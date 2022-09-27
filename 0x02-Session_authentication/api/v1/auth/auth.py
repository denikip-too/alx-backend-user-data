#!/usr/bin/env python3
"""Auth class"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path and excluded_paths"""
        if path is None or path not in excluded_paths:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        path_l = len(path)
        slash_path = True if path[path_l - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'
        for exec in excluded_paths:
            exec_l = len(exec)
            if exec_l == 0:
                continue
            if exec[exec_l - 1] != '*':
                if tmp_path == exec:
                    return False
            else:
                if exec[:-1] == path[:exec_l - 1]:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None - request"""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        if session_name is None:
            return None
        session_id = request.cookies.get(session_name)
        return session_id
