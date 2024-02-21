from flask import Blueprint

api = Blueprint('api', "PapiApi")

@api.route("/")
def root():
    return "API Papillon"

