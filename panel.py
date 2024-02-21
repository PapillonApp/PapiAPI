from flask import Blueprint, send_from_directory

panel = Blueprint('panel', "PapiApi")

@panel.route("/panel")
def root():
    return send_from_directory("panel", "index.html")

