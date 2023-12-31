#!/usr/bin/python3
"""
    The `status` function returns a JSON response with the status "OK".
    :return: a JSON response with the status "OK".
"""


from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def object_by_type():
    """
    The function `object_by_type` returns a JSON object containing
    the count of different types of
    objects in a storage.
    :return: a JSON object that contains the counts of different types
    of objects in the storage.
    """
    return jsonify(
        {
            "amenities": storage.count("3"),
            "cities": storage.count("5"),
            "places": storage.count("2"),
            "reviews": storage.count("3"),
            "states": storage.count("2"),
            "users": storage.count("3")
        })
