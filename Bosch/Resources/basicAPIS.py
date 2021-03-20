from flask_restful import Resource, reqparse, request

class sendImage(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('imageb64', help = 'This field cannot be blank', required = True)
        parser.add_argument('rotation', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()
        return {
            "message" : "Received Req successfully",
            "image" : f"{data['imageb64'][:100]}",
            "rotation" : data['rotation']
        }
    def get(self):
        return {"message" : "Please post method to send image"}