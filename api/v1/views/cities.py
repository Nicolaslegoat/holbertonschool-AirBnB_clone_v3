#!/usr/bin/python3
"""Cities"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.state import State
from models.state import City


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_cities(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=["GET"])
def get_city(city_id):
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    else:
        return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    else:
        storage.delete(city)
        storage.save()

    return jsonify({}), 200


@app_views.route("/states/<state_id>/cities", methods=["POST"],
                 strict_slashes=False)
def post_city(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    body = request.get_json()
    if body is None:
        abort(400, "Not a JSON")

    if "name" not in body:
        abort(400, "Missing name")

    city = City(state_id=state_id, **body)
    storage.new(city)
    storage.save()

    return jsonify(city.to_dict()), 201


@app_views.route("/cities/<city_id>", methods=["PUT"])
def update_city(city_id):
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    else:
        request_http = request.get_json()
        if request_http is None:
            abort(400, 'Not a JSON')

    for key, value in request_http.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, key, value)

    storage.save()

    return jsonify(city.to_dict()), 200
