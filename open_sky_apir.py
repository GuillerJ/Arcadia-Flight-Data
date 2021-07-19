from flask import Flask, request
from flask_restful import Resource, Api
from airports_example import airports
import requests

app = Flask(__name__)
api = Api(app)
open_sky_api = 'https://opensky-network.org/api/{}'
flights_arr = 'flights/arrival/{}'


class HelloWorld(Resource):
    def get(self):
        r = requests.get(open_sky_api.format(flights_arr), auth=('user', 'pass'))
        #print(r.json())
        return r.text() #{'hello': 'world'}

class get_airport_example(Resource):
    def get(self):
        return(airports)

api.add_resource(HelloWorld, '/')
api.add_resource(get_airport_example, '/exAir')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
