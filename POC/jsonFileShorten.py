# we are trying to shorten foodsurvey_edit.json to only the foods we use
import json
import csv
import pandas as pd


def shortenJson():
  # get all the food survey foods being used from foodtoFoodSurvey.csv
  foodSurveyFoods = []
  with open("./data/foodtoFoodSurvey.csv", "r") as file:
      reader = csv.reader(file)
      for row in reader:
          foodSurveyFoods.append(row[1])
  # open foodsurvey_edit.json
  with open("./data/foodsurvery_edit.json") as f:
      data = json.load(f)
      # loop through the data to find the food
      for food in data['SurveyFoods']:
          if food['description'] not in foodSurveyFoods:
              data['SurveyFoods'].remove(food)
      # save the shortened json file
      with open("./data/foodsurvery_edit.json", "w") as json_file:
          json.dump(data, json_file, indent=4)

def main():
    shortenJson()  

if __name__ == "__main__":
    main()
  


