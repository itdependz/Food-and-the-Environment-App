import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import plotly.express as px
import BarGraphDisplay

# Configure the Streamlit Page
st.set_page_config(
    page_title="PygWalker",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add a title
st.title("PygWalker")

# import your Data
df = pd.read_csv("./data/food-footprints.csv")

# Make the Entity column as a list
entities = df['Entity'].tolist()

# Generate the HTML using Pygwalker
pyg_html = pyg.walk(df, return_html=True)

#create bar chart using plotly
fig = px.bar(df, x='Entity', y='Emissions per kilogram', title='Food Footprint')

# Embed the generated HTML into the Streamlit App
components.html(pyg_html, width=1000, height=800, scrolling=True)

#embed the plotly chart into the Streamlit App
st.plotly_chart(fig, use_container_width=True)

options = st.multiselect(
    'Choose Foods You Want to Display',
    entities
    )
# Call the BarGraphDisplay function
st.plotly_chart(BarGraphDisplay.BarGraphDisplay(df, options))
