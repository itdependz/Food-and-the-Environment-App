import requests
import json

# Define the API endpoint URL
api_url = "https://www.themealdb.com/api/json/v1/1/search.php?s=pad_see_ew"  # Replace with the actual API URL

# Make a GET request to the API endpoint
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Save the JSON response to a file
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("Data saved to data.json")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")