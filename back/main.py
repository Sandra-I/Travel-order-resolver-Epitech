import json
from flask import Flask, jsonify, request 
from flask_cors import CORS, cross_origin
import source.TripEvaluation.main_eval as tp
import source.Itinerary.itinerary as it
import source.HereMap.GetYourRoute as map

app = Flask(__name__) 
CORS(app, resources=r'*')
# CORS(app, resources=r'https://travel-resolver-100.herokuapp.com/*')

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
        if tripArray != 'Invalid Sentence':
            print('tripArray', tripArray, len(tripArray))
            itinerary = it.get_itinerary(locArray = tripArray)
            print(f"reponse finale {itinerary}")

            test = ['Toulouse', 'Bordeaux']
            # test = [tripArray[0], tripArray[1]]
            print('test', test)
            mapItinerary = map.GetRoute(test[0], test[1])
            print(mapItinerary)
    
    return jsonify({
        'train': itinerary,
        'car': mapItinerary
    })

if __name__ == '__main__': 
    app.run(debug = True) 