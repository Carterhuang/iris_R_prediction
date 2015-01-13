from flask import Flask, jsonify, request, abort
import pyRserve
import r_client
from r_client import *


server = Flask(__name__)
r_client = RClient()

@server.route("/")
def index():
	index_file = open('index.html', 'r').read()
	return index_file

@server.route('/iris-predict/api/v1.0/predict', methods=['POST'])
def get_prediction():
    attributes = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 
        'Petal.Width', "Species"]
    attribute_vals = [request.get_json(force=True).get(k, 0) for k in attributes] 
    if sum(map(lambda x : 1 if x == 0 else 0, attribute_vals)) != 1:
        abort(400)
    
    sl, sw, pl, pw, species = attribute_vals
    species = str(species)
    if species == '0':
        prediction = r_client.predict_species(sl, sw, pl, pw)  
        return jsonify({'species' : prediction})
    else:
        p_attribute = ''
        try:
            p_attribute = attributes[attribute_vals.index(0)]
        except:
            abort(500)
 
        prediction = r_client.predict_attribute(p_attribute, species, sl, sw, pl, pw)
        return jsonify({p_attribute : prediction})
 
    return jsonify({'junk' : 'NULL'})

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=80)
