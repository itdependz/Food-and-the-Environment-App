import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import plotly.express as px
import csv
import utilities
import time

# Add a title
st.title("Food Composite Score Calculator")

# import your Data
df = pd.read_csv("./data/food-footprints.csv")


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

if submit:
    progress.progress(0)
    for i in range(100):
        progress.progress(i + 1, "calculating...")
        time.sleep(.01)
    time.sleep(1)
    progress.empty()
