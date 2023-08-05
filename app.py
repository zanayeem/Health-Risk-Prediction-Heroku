import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_bootstrap import Bootstrap
import pickle
import joblib

app = Flask(__name__)
Bootstrap(app)

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
    pulse = float(request.form.get('pulse'))
    blood = float(request.form.get('blood'))
    temp = float(request.form.get('temp'))
    age = float(request.form.get('age'))
    height_feet = float(request.form.get('height_feet'))
    height_inches = float(request.form.get('height_inches'))
    weight = float(request.form.get('weight'))*2.20462
    gender = float(request.form.get('gender'))

    height = (height_feet*12) + height_inches

    all_features = [pulse,blood,temp,age,height,weight,gender]
    all_features = [np.array(all_features)]
    final_features = scaler.transform(all_features)
    prediction = model.predict(final_features)
    #-------------------------------------------------

    #return render_template('index.html', prediction_text=f"Your Health Prediction: {prediction[0]}")
    return f"Your Health Prediction: {prediction[0]}"


if __name__ == "__main__":
    app.run(debug=False)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run(host="0.0.0.0", port=8080)

