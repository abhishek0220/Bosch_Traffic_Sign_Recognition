from flask_restful import Resource, reqparse, request

class TestAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()
        return {'message' : f"got {data['text']}"}
    
    def get(self):
        return "Hiiii"