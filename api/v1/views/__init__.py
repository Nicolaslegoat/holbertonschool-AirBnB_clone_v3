#!/usr/bin/python3
"""Initilaization for module to the API"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
