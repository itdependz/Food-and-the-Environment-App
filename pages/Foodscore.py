import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import plotly.express as px
import csv
from utilities import normalization, compositeNumConvert, compositeScoreGetter, BarGraphDisplay, rankedScoreSupplier, rankedScoreDataFrameSupplier, getNutrionalValue, translatetoFoodSurvey, getDishFromDB, justIngredients
import time
import math
import json
import sys
import os

# import a python file that is in the lib folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib import mathFunctions


# Add a title
st.title("Food Composite Score Calculator")

# import your Data
df = pd.read_csv("./data/food-footprints.csv")
compositeScoreDF = pd.read_csv("./data/compositevalue.csv")


# Make the Entity column as a list
entities = df['Entity'].tolist()

#Create the option to select the food
foodOptions = st.selectbox(
    'Choose Foods You Want to Display',
    entities
    )

# create a textbox to input the dish
dish = st.text_input("Enter the dish you want ingredients for")


# Create a button to sumbit the food
submit = st.button("Submit")

# Create a progress bar
progress = st.progress(0, "calculating...")
progress.empty()

# Lower Score Equals Better Score
emissionScore = compositeScoreGetter(foodOptions, "Emissions per kilogram")
landUseScore = compositeScoreGetter(foodOptions, "Land use per kilogram")
eutrophicationScore = compositeScoreGetter(foodOptions, "Eutrophication per kilogram")
waterScarcityScore = compositeScoreGetter(foodOptions, "Water scarcity per kilogram")
waterWithdrawalScore = compositeScoreGetter(foodOptions, "Water withdrawals per kilogram")
biodiversityScore = abs(2*compositeScoreGetter(foodOptions, "biodiversity_kg")-11)

# add up the values
compositeScore = (emissionScore + landUseScore + eutrophicationScore + waterScarcityScore + waterWithdrawalScore + biodiversityScore)/6

if submit:
    progress.progress(0)
    for i in range(100):
        progress.progress(i + 1, "calculating...")
        time.sleep(.01)
    time.sleep(1)
    progress.empty()
    rankScore = rankedScoreSupplier(foodOptions)
    # change the color of the text depending ont the rank
    
    if rankScore>=1 and rankScore<50:
        html_temp = """
    <head>
<style> 
.circle {
  width: 100px;
    height: 100px;
    background-color: #4CAF50;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    font-family: 'Roboto', sans-serif;
}

.text {
  color: white;
  font-size: 20px;
  margin-bottom: -10px
}
.scoreNum {
    color: white;
    font-size: 20px;
    }
</style>
</head>
<body>

<div class="circle">
  <p class="text">RANK</p>
  <p class="scoreNum">"""
        
        html_temp2 = """</p>
</div>

</body>
        """
        
        st.markdown(html_temp + str(rankScore) + html_temp2, unsafe_allow_html=True)
        st.markdown("## Composite Score: "+ str(mathFunctions.roundTo2Decimals(compositeScore)))
        st.write()
    elif rankScore>=50 and rankScore<150:
        html_temp = """
    <head>
<style> 
.circle {
  width: 100px;
    height: 100px;
    background-color: #dbc114;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    font-family: 'Roboto', sans-serif;
}

.text {
  color: white;
  font-size: 20px;
  margin-bottom: -10px
}
.scoreNum {
    color: white;
    font-size: 20px;
    }
</style>
</head>
<body>

<div class="circle">
  <p class="text">RANK</p>
  <p class="scoreNum">"""
        
        html_temp2 = """</p>
</div>

</body>
        """
        st.markdown(html_temp + str(rankScore) + html_temp2, unsafe_allow_html=True)
        st.markdown("## Composite Score: "+ str(mathFunctions.roundTo2Decimals(compositeScore)))
        st.write()
    else:
        html_temp = """
    <head>
<style> 
.circle {
  width: 100px;
    height: 100px;
    background-color: #bf0e0b;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    font-family: 'Roboto', sans-serif;
    margin-bttom: 10px;
}

.text {
  color: white;
  font-size: 20px;
  margin-bottom: -10px
}
.scoreNum {
    color: white;
    font-size: 20px;
    }
</style>
</head>
<body>

<div class="circle">
  <p class="text">RANK</p>
  <p class="scoreNum">"""
        
        html_temp2 = """</p>
</div>

</body>
        """
        st.markdown(html_temp + str(rankScore) + html_temp2, unsafe_allow_html=True)
        st.markdown("## Composite Score: "+ str(mathFunctions.roundTo2Decimals(compositeScore)), help="To learn How composite score is calculated, go to the *About* Page")
        st.write()
    # st.write(rankedScoreDataFrameSupplier())
    # get the nutrional value for the food
    #translate to foodsurvey
    translatedFood = translatetoFoodSurvey(foodOptions)
    nutrition = getNutrionalValue(translatedFood)
    if nutrition is None:
        st.markdown("## Nutrition: :red[Not Available]")
    else:
        st.markdown("## Nutrition: :green[Available]")
        st.markdown("<details close><summary><h3>Tier 1 Nutrion</summary><br>hi</details>", unsafe_allow_html=True)
        st.write(nutrition)
    ingredients = getDishFromDB(dish)
    # ingredientsList = justIngredients(dish)
    st.markdown("# Ingredients")
    st.write(ingredients)
    # st.write(ingredientsList)
        
        
