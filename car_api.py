import requests
import os

CAR_API_KEY = os.getenv("CAR_API_KEY")

def fetch_car_data(make=None, fuel_type=None):
    url = "https://api.api-ninjas.com/v1/cars"
    headers = {"X-Api-Key": CAR_API_KEY}
    params = {}

    if make:
        params["make"] = make
    if fuel_type:
        params["fuel_type"] = fuel_type

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()



