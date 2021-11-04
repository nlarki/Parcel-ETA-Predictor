from flask import Flask, request
import pickle
import numpy as np

model = pickle.load(open())


app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)
