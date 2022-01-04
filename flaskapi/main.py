import json
from flask import Flask, jsonify, request 
from flask_cors import CORS, cross_origin
  
app = Flask(__name__) 
# CORS(app)

CORS(app, resources=r'http://localhost:8080/*')
# CORS(app, resources=r'/api/*')

# CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Accept, Content-Type'

@app.route('/', methods = ['GET', 'POST']) 
@cross_origin() 
def home(): 
    if(request.method == 'POST'): 
        data = json.loads(request.data)
        print(data)
        # data = "hello world"
        return jsonify(data)
    return jsonify({'data': "toto"})

@app.route('/vocal/<string:data>', methods = ['POST'])
@cross_origin() 
def vocal(data): 
    print('data', data, type(data))
    return jsonify({'data': data})

@app.route('/home/<text>', methods = ['POST', 'GET', 'OPTIONS'])
# @cross_origin(allow_headers=['*'], send_wildcard=True) 
@cross_origin() 
def disp(): 
    data = json.loads(request.data)
    print(data)
        # data = "hello world"
    return jsonify(data)
  
  
if __name__ == '__main__': 
  
    app.run(debug = True) 