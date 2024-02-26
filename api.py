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

@api.route("/messages")
def disclaimerIE():
    with open("data/json/messages.json", "r") as file:
        messagesfile = json.load(file)
    return jsonify(messagesfile)

@api.route("/latestVersion/<string:platform>")
def latestVersion(platform):
    with open(f"data/json/latestVersion{platform}.json", "r") as file:
        latestVersionFile = json.load(file)
    return jsonify(latestVersionFile)

@api.route("/staff/<string:name>/photo")
def staffPhoto(name):
    filepath = f"data/img/staff_{name}.png"
    return send_file(filepath, mimetype='image/png')