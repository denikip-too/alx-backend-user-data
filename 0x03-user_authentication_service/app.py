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
def register_users(email: str, password: str) -> str:
    """Register user"""
    try:
        email = request.form['email']
        password = request.form['password']
    except ValueError:
        abort(404)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify(
                {"email": "<registered email>", "message": "user created"})
    return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
