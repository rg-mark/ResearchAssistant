import requests
import os

api_key = os.getenv("IEEE_API_KEY")
url = f"https://ieeexploreapi.ieee.org/api/v1/search/articles?apikey={api_key}&querytext=machine+learning&max_records=1&start_record=1"

response = requests.get(url)
print(response.status_code)
print(response.text)
