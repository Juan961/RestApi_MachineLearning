from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from utils import Model
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app) 

data_med = [
    # age 
    54,
    # sex 
    1, 	
    # cp 
    1,
    # trestbps 
    131,
    # chol 
    246, 	
    # fbs 
    0,
    # restcg 
    1,
    # thalach 
    150,
    # exang 
    0,
    # oldpeak 
    1,
    # slope 
    1,
    # ca 
    1,
    # th 
    2
]

model = Model()

class Predict(Resource):

    def post(self):
        try: 
            request_json = request.get_json()

            x = [[ request_json['age'], request_json['sex'], request_json['cp'], request_json['trestbps'], request_json['chol'], request_json['fbs'], request_json['restcg'], request_json['thalach'], request_json['exang'], request_json['oldpeak'], request_json['slope'], request_json['ca'], request_json['thal'] ]]

            result = model.predict(x)
    
            result = int(result[0])

            request_json.update({'Prediction': result })

            return jsonify(request_json)
        
        except AttributeError:
            resp = jsonify({'Error': 'No se encontraron datos'})

        except TypeError:
            resp = jsonify({'Error': 'No se recibio data en formato JSON'})
            resp.status_code = 400
            return resp

        except KeyError:
            resp = jsonify({'Datos invalidos': 'Porfavor ingrese una llave valida { "years" : 10 }'})
            resp.status_code = 400
            return resp
        
        except:
            resp = jsonify({'Error': 'Del servidor'})
            resp.status_code = 500
            return resp

api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
