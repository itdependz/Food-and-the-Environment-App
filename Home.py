import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import plotly.express as px
import csv
import utilities

reader = csv.reader(open('./data/food-footprints.csv'))

# Configure the Streamlit Page
st.set_page_config(
    page_title="Enviromental Footprints of Food",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🌏"
)

# Add a title
st.title("Enviromental Footprints of Food")


# import your Data
df = pd.read_csv("./data/food-footprints.csv")


# Make the Entity column as a list
entities = df['Entity'].tolist()


# Make a metric list
metrics = next(reader)

for i in metrics:
    if i == "Entity":
        metrics.remove(i)
        break

metricOption = st.selectbox(
    'Choose a Metric to Display',
    metrics
)

foodOptions = st.multiselect(
    'Choose Foods You Want to Display',
    entities
    )
# Call the BarGraphDisplay function
try:
    st.plotly_chart(utilities.BarGraphDisplay(df, foodOptions, metricOption))
except:
    st.write("Please select a metric and food to display")
    st.write("If you have selected a food and metric, please ensure the food is in the list of foods")

