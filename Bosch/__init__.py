from flask import Flask, url_for
from flask_restful import Api, Resource
from Bosch.preprocess_and_split import load_and_preprocess, train_valid_splitting
from Bosch.model import testModel, train_model

app = Flask(
    __name__,
    static_url_path='/static', 
    static_folder='static')

api = Api(app)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def hdfd():
    # input_data, input_labels = load_and_preprocess()
    # test_model = testModel()
    # test_model.summary()
    # X_train, X_valid, y_train, y_valid = train_valid_splitting(input_data, input_labels)
    # train_model(test_model, X_train, X_valid, y_train, y_valid)
    return f"Running..."

from Bosch.Resources import basicAPIS
api.add_resource(basicAPIS.sendImage, '/sendImage')
api.add_resource(basicAPIS.getAllClasses, '/allClasses')