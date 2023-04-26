
import requests
from flask import Flask, flash, make_response, render_template, request
from flask_restful import Api, Resource

app = Flask(__name__, template_folder="./templates")
api = Api(app)

# Define the Flask resource class for landing service


class LandingService(Resource):
    def get(self):
        return make_response(render_template('index.html'))

    def post(self):
        # Get the input values from the form in index.html
        first = int(request.form['first'])
        second = int(request.form['second'])
        operation = request.form['operation']

        # Call the respective microservice based on the selected operation
        if operation == 'add':
            response = requests.get(
                'http://addition-service:5001/addition/{}/{}'.format(first, second))
        elif operation == 'subtract':
            response = requests.get(
                'http://subtraction-service:5002/subtraction/{}/{}'.format(first, second))
        elif operation == 'multiply':
            response = requests.get(
                'http://multiplication-service:5003/multiplication/{}/{}'.format(first, second))
        elif operation == 'divide':
            response = requests.get(
                'http://division-service:5004/division/{}/{}'.format(first, second))
        elif operation == 'exponent':
            response = requests.get(
                'http://exponent-service:5005/exponent/{}/{}'.format(first, second))
        elif operation == 'modulus':
            response = requests.get(
                'http://modulus-service:5006/modulus/{}/{}'.format(first, second))
        elif operation == 'greaterthan':
            response = requests.get('http://greaterthan-service:5007/greaterthan/{}/{}'.format(first, second))
        else:
            return 'Invalid operation', 400

        if response.status_code == 200:
            result = response.json()['result']
            flash('Result: {}'.format(result))
        else:
            flash('Error: {}'.format(response.json()['error']))
        return make_response(render_template('index.html'))


api.add_resource(LandingService, '/')


if __name__ == '__main__':
    app.secret_key = 'supersecretkey' 
    print("HELLOOOO!!!!!!!!!!!")
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
