#!/usr/bin/python3
"""
Simple Flask API to manage users in memory.
"""

from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return the list of all usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return user data for a given username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the users dictionary."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    user_data = request.get_json()

    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
