from flask import Flask, url_for
from flask_restful import Api, Resource
from Bosch.preprocess_and_split import load_and_preprocess, train_valid_splitting
from Bosch.model import testModel, train_model
import time
from flask import jsonify
from flask_executor import Executor


app = Flask(
    __name__,
    static_url_path='/static', 
    static_folder='static')
executor = Executor(app)
api = Api(app)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['EXECUTOR_PROPAGATE_EXCEPTIONS'] = True 

def runP():
    input_data, input_labels = load_and_preprocess()
    test_model = testModel()
    #test_model.summary()
    X_train, X_valid, y_train, y_valid = train_valid_splitting(input_data, input_labels)
    train_model(test_model, X_train, X_valid, y_train, y_valid)
    return "DONE"


@app.route('/')
def mainRoute():
    #input_data, input_labels = load_and_preprocess()
    #test_model = testModel()
    # test_model.summary()
    #X_train, X_valid, y_train, y_valid = train_valid_splitting(input_data, input_labels)
    #train_model(test_model, X_train, X_valid, y_train, y_valid)
    executor.submit(runP)
    return f"Running..."
    
@app.route('/s')
def start_task():
    executor.submit_stored('calc_power', runP)
    return jsonify({'result':'success'})

@app.route('/g')
def get_result():
    if not executor.futures.done('calc_power'):
        return jsonify({'status': executor.futures._state('calc_power')})
    #future = executor.futures.pop('calc_power')
    return jsonify({'status': 'completed', 'result': executor.futures.result('calc_power')})

from Bosch.Resources import basicAPIS
api.add_resource(basicAPIS.sendImage, '/sendImage')
api.add_resource(basicAPIS.getAllClasses, '/allClasses')