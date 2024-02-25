import json
from flask import Blueprint, jsonify, send_file

api = Blueprint('api', "PapiApi")


@api.route("/")
def root():
        with open("data/json/api.json", "r") as file:
            apiFile = json.load(file)
        return jsonify(apiFile)
    
@api.route("/staff")
def staff():
    with open("data/json/staff.json", "r") as file:
        staffFile = json.load(file)
    return jsonify(staffFile)

@api.route("/warning")
def warning():
    with open("data/json/warning.json", "r") as file:
        warningFile = json.load(file)
    return jsonify(warningFile)

@api.route("/disclaimerIE")
def disclaimerIE():
    with open("data/json/disclaimerIE.json", "r") as file:
        disclaimerIEFile = json.load(file)
    return jsonify(disclaimerIEFile)


@api.route("/staff/<string:name>/photo")
def staffPhoto(name):
    filepath = f"data/img/staff_{name}.png"
    return send_file(filepath, mimetype='image/png')