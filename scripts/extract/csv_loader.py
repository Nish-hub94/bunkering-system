import pandas as pd

#loading the data
def load_csv(path):
    csv_data = pd.read_csv(path)
    #csv_data = pd.read_csv("data/fuel_deliveries.csv")
    print("CSV loaded")
    return csv_data

#cleaning dat

