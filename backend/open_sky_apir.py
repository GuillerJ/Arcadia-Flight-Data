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
            return "None"
        
        end = datetime.now()
        end_unix = int(time.mktime(end.timetuple()))
        begin = datetime.strptime(date, '%d %B %Y')
        begin_unix = int(time.mktime(begin.timetuple()))
        params = {'airport': airport, 'begin': begin_unix, 'end': end_unix} 
        r = requests.get(open_sky_api.format(flights_arr), params=params)
        try:
            data_json = r.json()
            data_dict = {}
            i = 0
            for data in data_json:
                data.update({'firstSeen': datetime.fromtimestamp(data.get('firstSeen')).strftime('%d-%m-%Y %H:%M:%S')})
                data.update({'lastSeen': datetime.fromtimestamp(data.get('lastSeen')).strftime('%d-%m-%Y %H:%M:%S')})
                data_dict[i] = data
                i += 1
        except:
            data_dict = {"Error": "Could not retrieve any data from open sky api. Api is busy."}
            print(r.text)
        
        return data_dict


api.add_resource(HelloWorld, '/')
api.add_resource(get_airport_example, '/exAir')
api.add_resource(get_arrivals, '/arrivals/<airport>/<date>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
