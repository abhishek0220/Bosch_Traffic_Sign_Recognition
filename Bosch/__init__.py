from flask import Flask, url_for
from flask_restful import Api, Resource
#from Bosch.preprocess import load_and_preprocess

app = Flask(__name__)

api = Api(app)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def hdfd():
    input_data, input_labels = load_and_preprocess()
    return f"Running... "

from Bosch.Resources import basicAPIS
api.add_resource(basicAPIS.sendImage, '/sendImage')