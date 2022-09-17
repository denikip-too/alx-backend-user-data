#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def index() -> str:
    """return a JSON payload"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def register_users() -> str:
    """Register user"""
    email = request.form['email']
    password = request.form['password']
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"})
    else:
        return jsonify(
                {"email": "<registered email>", "message": "user created"})


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> str:
    """Log in"""
    email = request.form['email']
    password = request.form['password']
    try:
        user_login = AUTH.valid_login(email, password)
    except ValueError:
        abort(401)
    else:
        return jsonify({"email": "<user email>", "message": "logged in"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
