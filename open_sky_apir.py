from flask import Flask, request, abort
from flask_restful import Resource, Api
from functools import wraps
from datetime import datetime
from airports_example import airports
import requests, time

app = Flask(__name__)
api = Api(app)
open_sky_api = 'https://opensky-network.org/api/{}'
flights_arr = 'flights/arrival/'

def require_apikey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        with open('api.key', 'r') as apikey:
            key=apikey.read().replace('\n', '')
        if request.headers.get('api-key') and request.headers.get('api-key') == key:
            return view_function(*args, **kwargs)
        else:
            return abort(401)
    return decorated_function
    

class HelloWorld(Resource):
    @require_apikey
    def get(self):
        r = requests.get(open_sky_api.format(flights_arr), auth=('user', 'pass'))
        #print(r.json())
        return r.text() #{'hello': 'world'}

class get_airport_example(Resource):
    @require_apikey
    def get(self):
        return (airports)


class get_arrivals(Resource):
    @require_apikey
    def get(self, airport, date):
        if (airport == "None") or (date == "None"):
            return -1

        end = datetime.now()
        end_unix = int(time.mktime(end.timetuple()))
        begin = datetime.strptime(date, '%d %B %Y')
        begin_unix = int(time.mktime(begin.timetuple()))

        params = {'airport': airport, 'begin': begin_unix, 'end': end_unix} 
        r = requests.get(open_sky_api.format(flights_arr), params=params)
        print (params)
        print(open_sky_api.format(flights_arr))
        
        data_json = r.json()

        
        return (airports)


api.add_resource(HelloWorld, '/')
api.add_resource(get_airport_example, '/exAir')
api.add_resource(get_arrivals, '/arrivals/<airport>/<date>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
