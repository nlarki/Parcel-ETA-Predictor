from flask import Flask, request, render_template
import pickle
import numpy as np
import datetime

GB = pickle.load(
    open('ParcelLab-Task\JupyterNotebook\GradientBoosting.sav', 'rb'))
RF = pickle.load(open('ParcelLab-Task\JupyterNotebook\RandomForest.sav', 'rb'))


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/boosting', methods=['POST', 'GET'])
def boosting():
    delivery_region = request.form['a']
    courier = request.form['b']
    zip_code = request.form['c']
    return_tracking = request.form['d']
    delivery_location = request.form['e']
    Epoch_transit_date = request.form['f']
    Epoch_created_date = request.form['g']
    Epoch_pickup_date = request.form['h']
    arr = np.array([[delivery_region, courier, zip_code, return_tracking,
                     delivery_location, Epoch_transit_date, Epoch_created_date, Epoch_pickup_date]])
    GBpred = GB.predict(arr)
    GBpred = datetime.datetime.fromtimestamp(GBpred)


if __name__ == "__main__":
    app.run(debug=True)
