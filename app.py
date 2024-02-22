import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

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

# Generate the HTML using Pygwalker
pyg_html = pyg.walk(df, return_html=True)

# Embed the generated HTML into the Streamlit App
components.html(pyg_html, width=1000, height=800, scrolling=True)