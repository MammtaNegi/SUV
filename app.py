# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:40:48 2021

@author: Mamta
"""
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('decison_tree_classifier.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/result", methods=['POST'])
def predict():
    if request.method == 'POST':
        values = request.form
        prediction=model.predict(values)
        output=prediction[0]
        if output==1:
            return render_template('result.html',prediction_text="The customer seems to buy a SUV {}".format(output))
        else:
            return render_template('result.html',prediction_text="The customer will not buy a SUV {}".format(output))
if __name__=="__main__":
    app.run(debug=True)
