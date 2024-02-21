import json
from flask import Blueprint, jsonify

api = Blueprint('api', "PapiApi")


@api.route("/")
def root():
        with open("data/api.json", "r") as file:
            apiFile = json.load(file)
        return jsonify(apiFile)
    
@api.route("/staff")
def staff():
    with open("data/staff.json", "r") as file:
        staffFile = json.load(file)
    return jsonify(staffFile)

@api.route("/warning")
def warning():
    with open("data/warning.json", "r") as file:
        warningFile = json.load(file)
    return jsonify(warningFile)

@api.route("/disclaimerIE")
def disclaimerIE():
    with open("data/disclaimerIE.json", "r") as file:
        disclaimerIEFile = json.load(file)
    return jsonify(disclaimerIEFile)