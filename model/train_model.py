#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# dataset: https://www.kaggle.com/datasets/cedricaubin/ai-ml-salaries?resource=download
"""
Created on Wed Nov 16 18:29:38 2022

@author: jraposoneto
"""
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score, train_test_split

# funçao para treinar o modelo. Output: pipeline em .pkl e resultado da validaçao cruzada
def train_model(X, y):
    
    # split de treino e teste
    Xtr, Xts, ytr, yts = train_test_split(X, y, test_size = .3, random_state = 1)
    
    # create model pipeline
    pipe = Pipeline([('OrdinalEncoder', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-999)),
                     ('DecisionTreeRegressor', DecisionTreeRegressor(max_depth = 4, random_state=1))])

    # 5 Fold CV MAE
    mae = cross_val_score(pipe, Xtr, ytr, cv = 5, scoring='neg_mean_absolute_error')
    
    # registra a metrica alvo em um .txt
    with open("metricas.txt", "w") as text_file:
        text_file.write("MAE medio de validacao 5FCV: %s" % (np.mean(mae)/np.mean(ytr)))
        
    # treinamento do modelo
    pipe.fit(Xtr.values, ytr.values)
    
    # salvo meu dataset de teste OOS contendo x e y
    df = pd.concat([Xts, yts])
    
    # funcao retorna a base de dados e o pipeline
    return df.to_csv('/home/jraposoneto/gcp_deploy/data/test.csv'), joblib.dump(pipe, 'pipeline.pkl')

if __name__ == '__main__':
    
    # Carregando os dados
    df = pd.read_csv('/home/jraposoneto/gcp_deploy/data/salaries.csv', 
                     index_col=('work_year'), parse_dates=['work_year']).drop(['salary_currency', 'salary'],axis=1)

    # separando variavel alvo (y)
    X = df.drop(['salary_in_usd'], axis = 1)
    y = df.salary_in_usd
    
    # executo a funçao train_model
    train_model(X, y)
    
    