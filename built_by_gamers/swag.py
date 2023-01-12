
#%%
import pandas as pd
import requests
import json

# Set up the API URL
api_url = "https://www.googleapis.com/youtube/v3/search"
# Set up the API key
api_key = "AIzaSyDvktLRsAJVcvOYfKst7I5D1ulJHu2f68c"


def tube_stats(search_term):
    # Set up the search parameters
    params = {
    "part": "snippet",
    "q": search_term,
    "type": "video",
    "key": api_key,
    "timePeriod": "P7D"
    }
    # Make the API request
    response = requests.get(api_url, params=params)
    # Get the search volume
    search_volume = response.json()["pageInfo"]["totalResults"]
    # sv = response.json()["searchVolume"][0]["searchVolume"]
    print(response.json())

    # Print the search volume
    # print(f"The search volume for the keyword '{Pokemon}' is: {search_volume} ")
    return search_term

# def format_json(json_data):
    
#     json_object = json.loads(json_data)

#     json_formatted_str = json.dumps(json_object, indent=2)

#     return json_formatted_str

response = tube_stats("swaggy")
# pretty = format_json(response)

print(response)
# format_json()
data = pd.json_normalize(response)
print(data)

# %%






