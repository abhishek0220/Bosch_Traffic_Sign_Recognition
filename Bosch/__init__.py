from flask import Flask, url_for
from flask_restful import Api, Resource
#from Bosch.preprocess import load_and_preprocess
from Bosch.model import testModel

app = Flask(__name__)

api = Api(app)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def hdfd():
    #input_data, input_labels = load_and_preprocess()
    test_model = testModel()
    test_model.summary()
    return f"Running..."

from Bosch.Resources import basicAPIS
api.add_resource(basicAPIS.sendImage, '/sendImage')