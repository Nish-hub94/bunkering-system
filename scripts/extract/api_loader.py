import requests
import pandas as pd

def load_api(url):
    #url = "http://127.0.0.1:5000/fuel_prices"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        print("API Loaded")
        return df
    else:
        print("API request failed")
        return None


