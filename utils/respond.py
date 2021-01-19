from flask import jsonify
from errors.errors import InternalServerError


def make_err_response(err):
    return jsonify({"message": err.message if err.message else InternalServerError.message, "status": "ERROR"}), err.status_code if err.status_code else InternalServerError.status_code


def make_response(data, message, status_code=200):
    return jsonify({"data": data, "message": message, "status": "OK"}), status_code
