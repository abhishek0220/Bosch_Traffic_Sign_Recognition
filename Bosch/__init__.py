from flask import Flask, url_for
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

@app.route('/')
def hdfd():
    return f"Running... "

from Bosch.Resources import basicAPIS
api.add_resource(basicAPIS.sendImage, '/sendImage')