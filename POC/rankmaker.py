import pandas as pd
import math

def main():
#loop through all the entities and get the rank, add it to a new csv file
    df = pd.read_csv("./data/food-footprints.csv")
    entities = df['Entity'].tolist()
    rankedScores = []
    for entity in entities:
        print(entity)
        rankedScores.append(rankedScoreSupplier(entity))
    af = pd.DataFrame({'Entity': entities, 'rank': rankedScores})
    af.to_csv("./data/foodrankedFinal.csv", index=False)
    
def rankedScoreSupplier(food) -> int:
    emissionDF = pd.read_csv("./data/emissionsrankedfinal.csv")
    eutriphicationDF = pd.read_csv("./data/eutriphicationrankedfinal.csv")
    landUseDF = pd.read_csv("./data/landuserankedfinal.csv")
    waterScarcityDF = pd.read_csv("./data/waterscarcityrankedfinal.csv")
    waterWithdrawalDF = pd.read_csv("./data/waterwithdrawlrankedfinal.csv")
    biodiversityDF = pd.read_csv("./data/biodiversityrankedfinal.csv")
    
    #grab the rank from each dataframe based on the food and average them
    try:
        rank = (emissionDF.loc[emissionDF['Entity'] == food, 'rank'].values[0] + eutriphicationDF.loc[eutriphicationDF['Entity'] == food, 'rank'].values[0] + landUseDF.loc[landUseDF['Entity'] == food, 'rank'].values[0] + waterScarcityDF.loc[waterScarcityDF['Entity'] == food, 'rank'].values[0] + waterWithdrawalDF.loc[waterWithdrawalDF['Entity'] == food, 'rank'].values[0] + biodiversityDF.loc[biodiversityDF['Entity'] == food, 'rank'].values[0]) / 6
    except:
        print("The ranking for this food may be innacurate due to inadequate data.")
        rank = 200
    return math.floor(rank)

if __name__ == "__main__":
    main()

