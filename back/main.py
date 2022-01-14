import json
from flask import Flask, jsonify, request 
from flask_cors import CORS, cross_origin
  
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
    print('data', data, type(data))
    return jsonify({'receivedText': data['text']})

if __name__ == '__main__': 
    app.run(debug = True) 