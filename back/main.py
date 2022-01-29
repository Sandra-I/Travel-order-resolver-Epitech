import json
from flask import Flask, jsonify, request 
from flask_cors import CORS, cross_origin
import source.TripEvaluation.main_eval as tp
import source.Itinerary.itinerary as it

app = Flask(__name__) 
CORS(app, resources=r'https://travel-resolver-100.herokuapp.com/*')

@app.route('/', methods = ['GET']) 
@cross_origin() 
def home():
    return jsonify({'data': "Welcome!"})

@app.route('/vocal', methods = ['POST'])
@cross_origin()
def vocal():
    data = json.loads(request.data)
    phrase = str(data['text'])
    print('data', phrase, type(phrase))
    if phrase:
        tripArray = tp.main_test(phrase)
        if tripArray != 'Invalid Sentence':
            print(tripArray)
            itinerary = it.get_itinerary(locArray = tripArray)
            print(f"reponse finale {itinerary}")
    
    return jsonify({'data': itinerary})

if __name__ == '__main__': 
    app.run(debug = True) 