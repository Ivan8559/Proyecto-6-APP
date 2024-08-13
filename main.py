import joblib
import warnings
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS


model = joblib.load("modelo.pkl")
warnings.filterwarnings("ignore")

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods = ['POST'])
def predict():

    data = request.json
    print(data)

    data_values = [
        data['Category'],
        data['Type'],
        data['Content Rating'],
        data['Genres']
    ]

    prediction = model.predict([data_values])[0]
    #prediction = int(prediction)
    #print("La aplicacion tendra",round(prediction,1), "Estrellas")
    
    msg = "La aplicacion tendra",round(prediction,1), "Estrellas"

    return jsonify({
        'msg': msg,
        'prediction': prediction
    })

if __name__ == "__main__":
    app.run(port=8000, debug=True)