from flask import Flask
from flask_cors import CORS
from api import api
from panel import panel






papiApi = Flask("PapiApi")
CORS(papiApi)
papiApi.register_blueprint(api)
papiApi.register_blueprint(panel)


if __name__ == "__main__":
    papiApi.run(debug=True)
