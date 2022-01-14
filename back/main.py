import json
from flask import Flask, jsonify, request 
from flask_cors import CORS, cross_origin
# import sys
# sys.path.append('/home/sandra/Epitech_Project/T-AIA-901/tor_msc2022_group-100/back/source/TripEvaluation') 
import source.TripEvaluation.main_eval as tp
import source.Itinerary.itinerary as it

app = Flask(__name__) 
CORS(app, resources=r'http://localhost:8080/*')

@app.route('/', methods = ['GET', 'POST']) 
@cross_origin() 
def home():
    print('home') 
    if(request.method == 'POST'): 
        data = json.loads(request.data)
        print('data', data, type(data))
        return jsonify({'receivedText': data['text']})
    return jsonify({'data': "toto"})

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