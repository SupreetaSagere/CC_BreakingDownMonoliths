from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class DivisionResource(Resource):
    def get(self, number1, number2):
        result = number1 / number2
        return {'result': result}

api.add_resource(DivisionResource, '/division/<int:number1>/<int:number2>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
