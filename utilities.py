import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import plotly.express as px
import csv
import math

def BarGraphDisplay(df, foodList, targetMetric):
    # Get the corresponding cell to the item in the list under Emissions PEr kilogram
    ylist = []
    for item in foodList:
        num = (float(df[df['Entity'] == item][targetMetric].values[0]))
        ylist.append(num)
    fig = px.bar(df, x=foodList, y=ylist, title='Food Footprint', labels={'x': 'Food', 'y':targetMetric})
    
    return fig

def normalization(num, min, max):
    return (num - min) / (max - min)

def compositeNumConvert(num):
    if(int(num*10) == 10):
        return int(num*10)
    return int(num*10)+1

def compositeScoreGetter(food, factor):
    df = pd.read_csv("./data/compositevalue.csv")
    print(df.loc[df['Entity']==food, factor])
    return df.loc[df['Entity'] == food, factor].values[0]
    # with open("./data/compositevalue.csv", "r") as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         if row[0] == food:
    #             return df.loc[row, factor]

def rankedScoreSupplier(food) -> int:
    emissionDF = pd.read_csv("./data/emissionsrankedfinal.csv")
    eutriphicationDF = pd.read_csv("./data/eutriphicationrankedfinal.csv")
    landUseDF = pd.read_csv("./data/landuserankedfinal.csv")
    waterScarcityDF = pd.read_csv("./data/waterscarcityrankedfinal.csv")
    waterWithdrawalDF = pd.read_csv("./data/waterwithdrawlrankedfinal.csv")
    biodiversityDF = pd.read_csv("./data/biodiversityrankedfinal.csv")
    
    #grab the rank from each dataframe based on the food and average them
    rank = (emissionDF.loc[emissionDF['Entity'] == food, 'rank'].values[0] + eutriphicationDF.loc[eutriphicationDF['Entity'] == food, 'rank'].values[0] + landUseDF.loc[landUseDF['Entity'] == food, 'rank'].values[0] + waterScarcityDF.loc[waterScarcityDF['Entity'] == food, 'rank'].values[0] + waterWithdrawalDF.loc[waterWithdrawalDF['Entity'] == food, 'rank'].values[0] + biodiversityDF.loc[biodiversityDF['Entity'] == food, 'rank'].values[0]) / 6
    return math.floor(rank)