#!/usr/bin/python3
"""Module containing status endpoint for the API v1"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """return the status of the API"""
    return jsonify({"status": "OK"})
