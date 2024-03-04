import math
import numpy as np
import plotly.express as px
import pandas as pd
from utilities import normalization, compositeNumConvert

emissions = 0.0
landuse = 0.0
eutriphication = 0.0
waterscarcity = 0.0
waterwithdrawal = 0.0
biodiversity = 0.0

factors = [emissions, landuse, eutriphication, waterscarcity, waterwithdrawal, biodiversity]

df = pd.read_csv("./data/food-footprints.csv")
normalizedDF = pd.read_csv("./data/normalizeddata.csv")
compositeScoreDF = pd.read_csv("./data/compositeScore.csv")


# find the max value and min value in the emissions column
maxEmissions = df['Emissions per kilogram'].max()
minEmissions = df['Emissions per kilogram'].min()

# find the max value and min value in the land use column
maxLandUse = df['Land use per kilogram'].max()
minLandUse = df['Land use per kilogram'].min()

# find the max value and min value in the eutriphication column
maxEutriphication = df['Eutrophication per kilogram'].max()
minEutriphication = df['Eutrophication per kilogram'].min()

# find the max value and min value in the water scarcity column
maxWaterScarcity = df['Water scarcity per kilogram'].max()
minWaterScarcity = df['Water scarcity per kilogram'].min()

# find the max value and min value in the water withdrawal column
maxWaterWithdrawal = df['Water withdrawals per kilogram'].max()
minWaterWithdrawal = df['Water withdrawals per kilogram'].min()

# find the max value and min value in the biodiversity column
maxBiodiversity = df['biodiversity_kg'].max()
minBiodiversity = df['biodiversity_kg'].min()

#normalize the values for all the facotrs in the normalized data csv file
normalizedDF['Emissions per kilogram'] = normalizedDF['Emissions per kilogram'].apply(lambda x: normalization(x, minEmissions, maxEmissions))  
normalizedDF['Land use per kilogram'] = normalizedDF['Land use per kilogram'].apply(lambda x: normalization(x, minLandUse, maxLandUse))
normalizedDF['Eutrophication per kilogram'] = normalizedDF['Eutrophication per kilogram'].apply(lambda x: normalization(x, minEutriphication, maxEutriphication))
normalizedDF['Water scarcity per kilogram'] = normalizedDF['Water scarcity per kilogram'].apply(lambda x: normalization(x, minWaterScarcity, maxWaterScarcity))
normalizedDF['Water withdrawals per kilogram'] = normalizedDF['Water withdrawals per kilogram'].apply(lambda x: normalization(x, minWaterWithdrawal, maxWaterWithdrawal))
normalizedDF['biodiversity_kg'] = normalizedDF['biodiversity_kg'].apply(lambda x: normalization(x, minBiodiversity, maxBiodiversity))

#save the normalized data to a csv file
normalizedDF.to_csv('normalizedvalues.csv', index=False)

normalDF = pd.read_csv('normalizedvalues.csv')

#calculate the composite score for the selected food item
compositeScoreDF['Emissions per kilogram'] = normalDF['Emissions per kilogram'].apply(lambda x: compositeNumConvert(x))
compositeScoreDF['Land use per kilogram'] = normalDF['Land use per kilogram'].apply(lambda x: compositeNumConvert(x))
compositeScoreDF['Eutrophication per kilogram'] = normalDF['Eutrophication per kilogram'].apply(lambda x: compositeNumConvert(x))
compositeScoreDF['Water scarcity per kilogram'] = normalDF['Water scarcity per kilogram'].apply(lambda x: compositeNumConvert(x))
compositeScoreDF['Water withdrawals per kilogram'] = normalDF['Water withdrawals per kilogram'].apply(lambda x: compositeNumConvert(x))
compositeScoreDF['biodiversity_kg'] = normalDF['biodiversity_kg'].apply(lambda x: compositeNumConvert(x))

#save the composite score to a csv file
compositeScoreDF.to_csv('compositevalue.csv', index=False)
# Print this when done
print("Everything converted")
