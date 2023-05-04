'''
This app file is used for setting routes like home page and results page, 
and handling POST requests from the file request.py.
'''

from flask import Flask, render_template, redirect, request, url_for
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results',methods=['POST'])
def results():
    # need to set this condition so redirect function can work properly
    if request.method == 'POST':
        radius_mean = float(request.form['radius_mean'])
        perimeter_mean = float(request.form['perimeter_mean'])
        area_mean = float(request.form['area_mean'])
        concavity_mean = float(request.form['concavity_mean'])
        concave_points_mean = float(request.form['concave_points_mean'])
        radius_worst = float(request.form['radius_worst'])
        perimeter_worst = float(request.form['perimeter_worst'])
        area_worst = float(request.form['area_worst'])
        concave_points_worst = float(request.form['concave_points_worst'])
        
        request_values = {'radius_mean':radius_mean, 'perimeter_mean': perimeter_mean, 'area_mean':area_mean, 'concavity_mean': concavity_mean,
                        'concave points_mean': concave_points_mean, 'radius_worst': radius_worst, 'perimeter_worst': perimeter_worst,
                        'area_worst': area_worst, 'concave points_worst': concave_points_worst}

        df_feature = pd.DataFrame(request_values, index=[0])
            
        # my model was trained with data in dataframes, so I needed to 
        # covert the user input into dataframe before running prediction    
        result = int(model.predict(df_feature)[0])
        
        # results are either 0 (for no cancer) and 1 (for having cancer)
        if result == 0:
            prediction = "Congrats, you don't have cancer!"
        else:
            prediction = "Sorry, you have cancer!"
    else:
        # this is for returning to the home page
        return render_template(url_for('home'))

    return render_template('results.html', prediction=prediction)

# route for requesting another prediction -> home page
@app.route('/restart')
def restart():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)