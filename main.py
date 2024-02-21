from flask import Flask
from api import api
from panel import panel

papiApi = Flask("PapiApi")
papiApi.register_blueprint(api)
papiApi.register_blueprint(panel)


if __name__ == "__main__":
    papiApi.run(debug=True)
