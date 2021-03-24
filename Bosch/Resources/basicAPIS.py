from flask_restful import Resource, reqparse, request
from flask import Response
from Bosch.push_image import pushImage
from Bosch.model import classes
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


class getAllClasses(Resource):
    def get(self):
        return {
            "message" : "OK",
            "classes" : classes
        }

class display_graph(Resource):
    
    pass