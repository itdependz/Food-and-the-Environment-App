import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import plotly.express as px
import csv
import math
import json
import ast
import requests

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
    if(math.floor(num*10) == 10):
        return math.floor(num*10)
    return math.ceil(num*10)

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
    try:
        rank = (emissionDF.loc[emissionDF['Entity'] == food, 'rank'].values[0] + eutriphicationDF.loc[eutriphicationDF['Entity'] == food, 'rank'].values[0] + landUseDF.loc[landUseDF['Entity'] == food, 'rank'].values[0] + waterScarcityDF.loc[waterScarcityDF['Entity'] == food, 'rank'].values[0] + waterWithdrawalDF.loc[waterWithdrawalDF['Entity'] == food, 'rank'].values[0] + biodiversityDF.loc[biodiversityDF['Entity'] == food, 'rank'].values[0]) / 6
    except:
        print("The ranking for this food may be innacurate due to inadequate data.")
        rank = 200
    return math.floor(rank)

def rankedScoreDataFrameSupplier():
    df = pd.read_csv("./data/sorted_rank.csv")
    return df

def getNutrionalValue(food_description):
    with open("./data/foodsurvery_edit.json") as f:
        data = json.load(f)
        # loop through the data to find the food
        for food in data['SurveyFoods']:
            if food['description'] == food_description:
                # print(f"Description: {food['description']}")
                nutritional_info = []
                for nutrient in food['foodNutrients']:
                    name = nutrient['nutrient']['name']
                    amount = nutrient['amount']
                    unit = nutrient['nutrient']['unitName']
                    nutritional_info.append(f"{name}: {amount} {unit}")
                return nutritional_info
        return None

def translatetoFoodSurvey(food):
    # open foodtoFoodSurvey.csv
    with open("./data/foodtoFoodSurvey.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == food:
                return row[1]

def getDishFromDB(food):
    # format the food where the first letter is capatilized, spaces are subsituted with _, and the rest of the letters are lower case
    food = food.lower()
    food = food.replace(" ", "_")
    food = food.capitalize()
    # Define the API endpoint URL
    api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={food}"
    # Make a GET request to the API endpoint
    response = requests.get(api_url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Save the JSON response to a file
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


def justIngredients(food):
     # format the food where the first letter is capatilized, spaces are subsituted with _, and the rest of the letters are lower case
    food = food.lower()
    food = food.replace(" ", "_")
    food = food.capitalize()
    ingredientsList = []
    # Define the API endpoint URL
    api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={food}"
    # Make a GET request to the API endpoint
    response = requests.get(api_url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        meal = response.json()

        # get the ingredients from the json file
        for i in range(0,21):
            if meal['meals'][f'strIngredient{i}'] != "" and meal['meals'][f'strIngredient{i}'] != None:
                ingredientsList.append((meal['meals'][f'strIngredient{i}']))
                
        return ingredientsList
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

