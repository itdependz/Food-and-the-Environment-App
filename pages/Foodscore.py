import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import plotly.express as px
import csv
from utilities import normalization, compositeNumConvert, compositeScoreGetter, BarGraphDisplay, rankedScoreSupplier, rankedScoreDataFrameSupplier
import time
import math

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
compositeScore = emissionScore + landUseScore + eutrophicationScore + waterScarcityScore + waterWithdrawalScore + biodiversityScore



if submit:
    progress.progress(0)
    for i in range(100):
        progress.progress(i + 1, "calculating...")
        time.sleep(.01)
    time.sleep(1)
    progress.empty()
    st.write("The composite score for " + foodOptions + " is " + str(compositeScore) + " and the rank score is " + str(rankedScoreSupplier(foodOptions)))
    st.write(rankedScoreDataFrameSupplier())
