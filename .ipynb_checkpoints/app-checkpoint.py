
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib

app = Flask(__name__)

model = pickle.load(open("health-predictor.pkl","rb"))
scaler = pickle.load(open("health-predictor-scaler.pkl","rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    int_features = [np.array(int_features)]
    final_features = scaler.transform(int_features)
    prediction = model.predict(final_features)

    #output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Your Health Prediction is {}'.format(prediction[0]))


if __name__ == "__main__":
    app.run(debug=True)
    app.config['PROPAGATE_EXCEPTIONS'] = True