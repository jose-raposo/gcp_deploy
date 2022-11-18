#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:28:42 2022

@author: jraposoneto
"""
import pandas as pd
import numpy as np
import joblib
from flask import Flask, request

# carregando o pipeline de regressao
model = joblib.load('model.pkl')

# criando o objeto Flask App
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return 'Voce acabou de realizar uma request do tipo GET. Envie uma POST request para /predict e obtenha as predicoes'

# criando backend da REST API com metodo POST
@app.route('/predict', methods = ['GET', 'POST'])
def run_model():
    
    if request.method == 'GET':
        return ''
    
    elif request.method == 'POST':
    
        # carregando os dados enviados por JSON application
        data = request.get_json()
        a = data['experience_level']
        b = data['employment_type']
        c = data['job_title']
        d = data['employee_residence']
        e = data['remote_ratio']
        f = data['company_location']
        g = data['company_size']
        
        # input
        load = np.array([[
            a, b, c, d, e, f, g]])
        
        # predicoes
        pred = model.predict(load)
        
        return 'Salario anual predito em USD: '+str(int(pred))
    
if __name__ == '__main__':
    app.run(debug = False)
