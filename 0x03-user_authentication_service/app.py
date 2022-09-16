#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


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
        user = AUTH.register_user(email, password)
    except NoResultFound:
        user = AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    else:
        abort(400)
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
