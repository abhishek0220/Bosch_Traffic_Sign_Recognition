from flask_restful import Resource, reqparse, request
from Bosch.push_image import PushImage
from Bosch.Graph.misclassified_samples import print_samples
# Send image API, Image in data dict
# Add categories option
class sendImage(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('imageb64', help = 'This field cannot be blank', required = True)
        parser.add_argument('rotation', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()
        image = data['imageb64']
        rotation = data['rotation']
        pushImage(image, 1, rotation)
        # Push into database with appropriate rotation
        return {
            "message" : "Received Req successfully",
            "image" : f"{data['imageb64'][:100]}",
            "rotation" : data['rotation']
        }
    def get(self):
        return {"message" : "Please post method to send image"}


class display_misclassified(Resource):
    #add a function for each graph
    def get(self):          #change to post
        if (True): #replace with condition for misclassified samples
            result = print_samples.basic(0); #instead of 0 pass the class chosen
            return {"message" : result["message"]}

    #misclassified samples - import the function from there and return the coordinates/graph