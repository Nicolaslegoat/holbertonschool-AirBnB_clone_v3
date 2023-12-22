#!/usr/bin/python3
"""Module containing status endpoint for the API v1"""


from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():

    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():

    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }

    return jsonify(stats)
