import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import plotly.express as px

def BarGraphDisplay(df, list):
    # Get the corresponding cell to the item in the list under Emissions PEr kilogram
    ylist = []
    for item in list:
        num = (float(df[df['Entity'] == item]['Emissions per kilogram'].values[0]))
        ylist.append(num)
    fig = px.bar(df, x=list, y=ylist, title='Food Footprint')
    
    return fig