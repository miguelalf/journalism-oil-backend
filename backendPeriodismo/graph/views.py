import os
import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def lists(request) :
    db_petrole_production = os.path.dirname(os.path.realpath(__file__)) + '/../../csv/petrole_production.csv'
    
    df_petrole_production = pd.read_csv(db_petrole_production)
    df_petrole_production = df_petrole_production.set_index('fecha')

    labels_petrole_production = list(df_petrole_production.columns)

    db_methane_derivates = os.path.dirname(os.path.realpath(__file__)) + '/../../csv/methane_derivates.csv'
    
    df_methane_derivates = pd.read_csv(db_methane_derivates)
    df_methane_derivates = df_methane_derivates.set_index('fecha')

    labels_methane_derivates = list(df_methane_derivates.columns)

    db_public_price = os.path.dirname(os.path.realpath(__file__)) + '/../../csv/public_price.csv'
    
    df_public_price = pd.read_csv(db_public_price)
    df_public_price = df_public_price.set_index('fecha')

    labels_public_price = list(df_public_price.columns)

    result = {
        'petrole_production': labels_petrole_production,
        'methane_derivates': labels_methane_derivates,
        'public_price': labels_public_price
    }

    return JsonResponse(result)

def corr(request) :
    db = os.path.dirname(os.path.realpath(__file__)) + '/../../csv/db_hydrocarbons.csv'

    df = pd.read_csv(db)
    df = df.set_index('fecha')

    new_df = df[request.GET.getlist('fields[]')]
    result = new_df.corr().to_json(orient="split")

    return JsonResponse(result, safe=False)