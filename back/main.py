import json
from flask import Flask, jsonify, request 
from flask_cors import CORS, cross_origin
import source.TripEvaluation.main_eval as tp
import source.Itinerary.itinerary as it
import source.HereMap.GetYourRoute as map
import copy

app = Flask(__name__) 
CORS(app, resources=r'https://travel-resolver-100.netlify.app/*')

@app.route('/', methods = ['GET']) 
@cross_origin() 
def home():
    return jsonify({'data': "Welcome!"})

@app.route('/vocal', methods = ['POST'])
@cross_origin()
def vocal():
    data = json.loads(request.data)
    phrase = str(data['text'])
    print('phrase received', phrase)
    if phrase:
        tripArray = tp.main_test(phrase)
        cities = copy.deepcopy(tripArray)
        if tripArray != 'Invalid Sentence':
            arrayFromMap = copy.deepcopy(tripArray)

            itinerary = it.get_itinerary(locArray = tripArray)
            print(f"reponse finale {itinerary}")

            mapItinerary = map.GetRoute(arrayFromMap)
            print(mapItinerary)
    
    return jsonify({
        'train': itinerary,
        'car': mapItinerary,
        'cities': cities
    })

if __name__ == '__main__': 
    app.run(debug = True) 