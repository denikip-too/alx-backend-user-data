#!/usr/bin/env python3
"""Route module for the API"""
from flask import jsonify, abort
from api.v1.app import auth


@app.route('/auth_session/login', methods=['POST'], strict_slashes=False)
@app.route('/api/v1/auth_session/login', methods=['POST'], strict_slashes=False)
def session_authentication() -> str:
    """handles all routes for the Session authentication"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None:
        return jsonify({ "error": "email missing" }), 400
    if password is None:
        return jsonify({ "error": "password missing" }), 400
    user 
