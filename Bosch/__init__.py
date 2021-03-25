from flask import Flask, url_for
from flask_restful import Api, Resource
from Bosch.preprocess_and_split import load_and_preprocess, train_valid_splitting
from Bosch.model import testModel, train_model
import time
from flask_cors import CORS, cross_origin
from flask import jsonify, request
from flask_executor import Executor
from Bosch.Graph.f1_score_per_class import get_f1_matrix

modelTraining = False

app = Flask(
    __name__,
    static_url_path='/static', 
    static_folder='static')
cors = CORS(app)
executor = Executor(app)
api = Api(app)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['EXECUTOR_PROPAGATE_EXCEPTIONS'] = True 

def trainModel(split_ratio):
    global modelTraining
    modelTraining = True
    start = time.time()
    input_data, input_labels = load_and_preprocess()
    test_model = testModel()
    #test_model.summary()
    X_train, X_valid, y_train, y_valid = train_valid_splitting(input_data, input_labels, split_ratio)
    train_model(test_model, X_train, X_valid, y_train, y_valid)
    modelTraining = False
    get_f1_matrix()
    return f"{int(time.time()-start)}s"

@app.route('/')
def mainRoute():
    return f"Running..."

@app.route('/trainModel')
def start_task():
    global modelTraining
    pkey = request.args.get('pkey', '').strip()
    if(pkey != '1234'):
        return jsonify({"message" : "Wrong Key", "status" : 401})
    if(modelTraining == True):
        modelTraining = False
    else:
        modelTraining = True
    return jsonify({"message" : "Training Started", "status" : 200})
    if not modelTraining:
        executor.submit_stored('modelTrain', trainModel)
        return jsonify({"message" : "Training Started", 'result':'success'})
    return jsonify({"message" : "Already in trainig"})
    

@app.route('/modelStatus')
def get_result():
    global modelTraining
    return jsonify({"running" : modelTraining})
    if not executor.futures.done('modelTrain'):
        return jsonify({'status': executor.futures._state('modelTrain')})
    #future = executor.futures.pop('modelTrain')
    return jsonify({'status': 'completed', 'result': executor.futures.result('modelTrain')})


from Bosch.Resources import basicAPIS
api.add_resource(basicAPIS.sendImage, '/sendImage')
api.add_resource(basicAPIS.display_misclassified, '/misclassified')
api.add_resource(basicAPIS.getAllClasses, '/allClasses')
api.add_resource(basicAPIS.display_graph_pcf, '/graphPCF')
api.add_resource(basicAPIS.randomVisual, '/imgGrid')
api.add_resource(basicAPIS.SIFTVisual,'/compareSIFT')
