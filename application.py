from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)

ridge_model = pickle.load(open('models/ridge_model.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/predictdata', methods=['GET', 'POST'])
def predictdata():

    if request.method == 'POST':

        Temperature = float(request.form['Temperature'])
        RH = float(request.form['RH'])
        Ws = float(request.form['Ws'])
        Rain = float(request.form['Rain'])
        FFMC = float(request.form['FFMC'])
        DMC = float(request.form['DMC'])
        ISI = float(request.form['ISI'])
        Classes = float(request.form['Classes'])
        Region = float(request.form['Region'])

        input_data = pd.DataFrame([[
            Temperature,
            RH,
            Ws,
            Rain,
            FFMC,
            DMC,
            ISI,
            Classes,
            Region
        ]], columns=[
            'Temperature',
            'RH',
            'Ws',
            'Rain',
            'FFMC',
            'DMC',
            'ISI',
            'Classes',
            'Region'
        ])

        scaled_data = standard_scaler.transform(input_data)

        result = ridge_model.predict(scaled_data)

        return render_template(
            'home.html',
            prediction_text=f'Predicted Fire Weather Index: {result[0]:.2f}'
        )

    return render_template('home.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)