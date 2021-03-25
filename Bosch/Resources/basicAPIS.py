from flask_restful import Resource, reqparse, request
from Bosch.Graph.misclassified_samples import print_samples
from flask import Response
from Bosch.push_image import pushImage
from Bosch.model import classes
from Bosch.Graph.per_class_frequency import plot_per_freq_class
from Bosch.Graph.random_visualizer import plotImages
from Bosch.Graph.failing_particular import show_SIFT_features
from flask import send_file
import base64

def imgPathtoB64(img_path: str):
    with open(img_path, "rb") as img_file:
        img_string = base64.b64encode(img_file.read())
    ib64 = img_string.decode()
    ib64 = f"data:image/jpeg;base64,{ib64}"
    return ib64


# Send image API, Image in data dict
# Add categories option -- done
class sendImage(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('imageb64', help = 'This field cannot be blank', required = True)
        parser.add_argument('rotation', help = 'This field cannot be blank', required = True)
        parser.add_argument('class', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()
        image = data['imageb64'].split(',')[1]
        rotation = int(data['rotation'])
        imgClass = int(data['class']) - 1
        if(pushImage(image, imgClass, rotation) == True):
            return {
            "message" : "Img added successfully successfully",
            'code' : 200
            }
        return Response("{'message': 'Some error occures'}", status=500, mimetype='application/json')
    def get(self):
        return {"message" : "Please post method to send image"}


class display_misclassified(Resource):
    #add a function for each graph
    def get(self):
        classLabel = int(request.args.get('class', 1))-1
        result = print_samples.basic(classLabel); #instead of 0 pass the class chosen
        for i in range(len(result)):
            result[i]['imgLink'] = imgPathtoB64(result[i]['ImageLoc'])
            result[i]['correct_label'] += 1
            result[i]['predicted_label'] += 1
        return {"results" : result}

    #misclassified samples - import the function from there and return the coordinates/graph
class getAllClasses(Resource):
    def get(self):
        return {
            "message" : "OK",
            "classes" : classes
        }

class display_graph_pcf(Resource):
    def get(self):
        img_coord = plot_per_freq_class()
        return {"coords" : img_coord, 'title' : 'Frequency Per Class'}
    
class randomVisual(Resource):
    def get(self):
        classLabel = int(request.args.get('class', 1))-1
        img_path = plotImages(classLabel)
        return {
            "imgLink" : imgPathtoB64(img_path)
        }

class SIFTVisual(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('path', help = 'This field cannot be blank', required = True)
        parser.add_argument('per', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()
        image_path_misclassified = data['path'] 
        misclassified_class = int(data['per']) -1
        img_path = show_SIFT_features.SIFT_compare(misclassified_class,image_path_misclassified)
        ret_val = {"img1":imagePathtoB64(img_path["Misclassified_Image"]), "img2":imagePathtoB64(img_path["Misclassified_for"])}
        return ret_val