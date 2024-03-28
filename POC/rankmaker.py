import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('./data/biodiversityranked.csv')

# Rank the numbers in the 'number' column
df['rank'] = df['biodiversity_kg'].rank()

df.to_csv('./data/biodiversityrankedfinal.csv', mode= 'a', index=False)
# Print the DataFrame
print(df)