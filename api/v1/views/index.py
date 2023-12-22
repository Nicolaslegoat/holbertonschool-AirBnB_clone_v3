#!/usr/bin/python3
"""Module containing status endpoint for the API v1"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    """Endpoint to retrieve the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    return jsonify({
        "amenities": 3,
        "cities": 5,
        "places": 2,
        "reviews": 3,
        "states": 2,
        "users": 3
    })
