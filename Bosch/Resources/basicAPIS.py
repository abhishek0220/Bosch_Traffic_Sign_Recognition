from flask_restful import Resource, reqparse, request

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
        
        # Push into database with appropriate rotation
        return {
            "message" : "Received Req successfully",
            "image" : f"{data['imageb64'][:100]}",
            "rotation" : data['rotation']
        }
    def get(self):
        return {"message" : "Please post method to send image"}


class display_graph(Resource):
    
    pass