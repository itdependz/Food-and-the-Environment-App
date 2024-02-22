import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import plotly.express as px
import BarGraphDisplay
df = pd.read_csv("./data/food-footprints.csv")
list = ["Beans"]
for item in list:
        print(df[df['Entity'] == item]['Emissions per kilogram'].values[0])