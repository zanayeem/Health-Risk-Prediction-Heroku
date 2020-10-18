
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib
import logging

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

app = Flask(__name__)
model = joblib.load("health-predictor.h5")
scaler = joblib.load("health-predictor-scaler.pkl")

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