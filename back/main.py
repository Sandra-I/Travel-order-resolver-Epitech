from http.client import HTTPResponse
import json
from flask import Flask, jsonify, request 
from flask_cors import CORS, cross_origin
import source.TripEvaluation.main_eval as tp
import source.Itinerary.itinerary as it
import requests as rq

app = Flask(__name__) 
CORS(app, resources={r"/foo": {"origins": "*"}})
# CORS(app, resources=r'http://localhost:8080/*')

@app.route('/', methods = ['GET']) 
@cross_origin() 
def home():
    print('home 2') 
    r = rq.get('https://httpbin.org/status/418')
    print(r.text)
    return jsonify({'data': "Welcome!"})

@app.route('/vocal', methods = ['POST'])
@cross_origin()
def vocal():
    print('vocal')
    data = json.loads(request.data)
    phrase = str(data['text'])
    print('data', phrase, type(phrase))
    if phrase:
        tripArray = tp.main_test(phrase)
    # Ajouter une validation avant de call cette méthode
        if tripArray != 'Invalid Sentence':
            print(tripArray)
            itinerary = it.get_itinerary(locArray = tripArray)
            print(f"reponse finale {itinerary}")
    
    return jsonify({'data': itinerary})

if __name__ == '__main__': 
    app.run(debug = True) 