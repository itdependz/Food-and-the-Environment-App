import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import plotly.express as px
import csv
import BarGraphDisplay

reader = csv.reader(open('./data/food-footprints.csv'))

# Configure the Streamlit Page
st.set_page_config(
    page_title="Enviromental Footprints of Food",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add a title
st.title("Enviromental Footprints of Food")


# import your Data
df = pd.read_csv("./data/food-footprints.csv")

# Setup the Pygwalker
# Generate the HTML using Pygwalker
pyg_html = pyg.walk(df, return_html=True)

# Embed the generated HTML into the Streamlit App
components.html(pyg_html, width=1000, height=800, scrolling=True)


# Make the Entity column as a list
entities = df['Entity'].tolist()


# Make a metric list
metrics = next(reader)

for i in metrics:
    if i == "Entity":
        metrics.remove(i)
        break


#create bar chart using plotly
fig = px.bar(df, x='Entity', y='Emissions per kilogram', title='Food Footprint')


#embed the plotly chart into the Streamlit App
st.plotly_chart(fig, use_container_width=True)

metricOption = st.selectbox(
    'Choose a Metric to Display',
    metrics
)

foodOptions = st.multiselect(
    'Choose Foods You Want to Display',
    entities
    )
# Call the BarGraphDisplay function
st.plotly_chart(BarGraphDisplay.BarGraphDisplay(df, foodOptions, metricOption))
