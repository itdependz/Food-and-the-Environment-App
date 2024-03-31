import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('./data/foodrankedFinal.csv')

# Sort the DataFrame by the 'column_name' column in ascending order
df = df.sort_values(by='rank', ascending=True)

# Write the sorted DataFrame to a new CSV file
df.to_csv('sorted_rank.csv', index=False)