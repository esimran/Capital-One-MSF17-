from flask import Flask, request, render_template
import scipy
import pandas as pd
import numpy as np
from sklearn.externals import joblib

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict-income', methods=['POST', 'GET'])
def predictIncome():
    if request.method == 'POST':
        result = request.form
        lat = result['lat']
        long = result['long']
        try:
            lat = int(lat)
        except:
            pass
        try:
            long = int(long)
        except:
            pass
        try:
            model = joblib.load('KNNeighborsRegressor.pkl')
            data = [lat, long]
            input_val = pd.DataFrame([data])
            prediction = model.predict(input_val)[0][0]
            prediction = round(prediction, 2)
        except Exception as e:
            print(e)
            prediction = "Invalid Input!"
        return render_template('income.html', prediction=prediction, lat=lat, long=long)


@app.route('/predict-price', methods=['POST', 'GET'])
def predictPrice():
    if request.method == 'POST':
        result = request.form
        lat = result['lat']
        long = result['long']
        try:
            lat = int(lat)
        except:
            pass
        try:
            long = int(long)
        except:
            pass
        try:
            model = joblib.load('PriceKNNeighborsRegressor.pkl')
            data = [lat, long]
            input_val = pd.DataFrame([data])
            prediction = model.predict(input_val)[0][0]
            prediction = round(prediction, 2)
        except Exception as e:
            print(e)
            prediction = "Invalid Input!"
        return render_template('price.html', prediction=prediction, lat=lat, long=long)


if __name__ == '__main__':
    app.run()