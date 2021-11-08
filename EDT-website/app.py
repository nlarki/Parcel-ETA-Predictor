from flask import Flask, request, render_template
import pickle
import numpy as np
import datetime

GB = pickle.load(
    open('GradientBoosting.pkl', 'rb'))
RF = pickle.load(open('RandomForest.pkl', 'rb'))


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
    Epoch_pickup_date = request.form['g']
    arr = np.array([[delivery_region, courier, zip_code, return_tracking,
                     delivery_location, Epoch_transit_date, Epoch_pickup_date]])
    GBpred = GB.predict(arr)
    GBpred = GBpred.item(0)
    GBresult = GBpred/1000
    GBresult = datetime.datetime.fromtimestamp(GBresult)

    return render_template('index.html', pred=format(GBresult))


@app.route('/forest', methods=['POST', 'GET'])
def forest():
    delivery_region = request.form['1']
    courier = request.form['2']
    zip_code = request.form['3']
    return_tracking = request.form['4']
    delivery_location = request.form['5']
    Epoch_transit_date = request.form['6']
    Epoch_pickup_date = request.form['7']
    arr = np.array([[delivery_region, courier, zip_code, return_tracking,
                     delivery_location, Epoch_transit_date, Epoch_pickup_date]])
    Fpred = RF.predict(arr)
    Fpred = Fpred.item(0)
    Fresult = Fpred/1000
    Fresult = datetime.datetime.fromtimestamp(Fresult)

    return render_template('index.html', pred1=format(Fresult))


if __name__ == "__main__":
    app.run(debug=True)
