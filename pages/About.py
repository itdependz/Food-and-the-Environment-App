import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import plotly.express as px
import csv
import utilities

# Add a title
st.title("About this Project")

st.markdown("## Purpose")
st.markdown("## The 5 Factors")
st.markdown("## Composite Scores")
st.markdown("To help understand the environmental impact of the food we eat, we can look at the composite score of the item.\
 There are two types of composite scores that users can look at, the full composite score and the ranked composite score.")
st.markdown("### Full Composite Score")
st.markdown("Full composite Score takes 5 factors including Emissions per kg, Land use per kg, Eutrophication per kg, Water scarcity per kg, Water withdrawals per kg, and Biodiversity per kg.\
            For each of the 5 factors we normalize the data and multiply the number by 10 to get a value from 1-10 of each of the 5 catagories. From there we average the 5 values to get the \
            composite score. The lower the composite score means the food has a **better** impact on the environment.")         
st.markdown("### Ranked Composite Score")
st.markdown("Ranked Composite Score takes the normalized values in each of the 5 catagories and ranks them from 1-N where 1 is the best and N is the worst. We then average these values to get \
            a final ranked composite score. The lower the ranked composite score means the food has a **better** impact on the environment.")  