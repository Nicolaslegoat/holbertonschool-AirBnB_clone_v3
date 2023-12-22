#!/usr/bin/python3
"""Defines the API actions for State objects"""

from flask import Flask, abort, request, jsonify
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    States = storage.all(State)
    dict_json = []
    for state in States.values():
        dict_json.append(state.to_dict())
    return jsonify(dict_json)


@app_views.route('/states/<state_id>', methods=["GET"], strict_slashes=False)
def get_states_id(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    else:
        return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object with id"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    else:
        storage.delete(state)
        storage.save()

    return jsonify({}), 200


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def post_state():
    """Creates a State"""
    body = request.get_json()

    if body is None:
        abort(400, "Not a JSON")

    if "name" not in body:
        abort(400, "Missing name")

    state = State(**body)
    storage.new(state)
    storage.save()

    return jsonify(state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """Updates a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    else:
        request_http = request.get_json()
        if request_http is None:
            abort(400, 'Not a JSON')

    for key, value in request_http.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)

    storage.save()

    return jsonify(state.to_dict()), 200
