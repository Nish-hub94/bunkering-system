import pandas as pd

def load_excel(path):
    excel_data = pd.read_excel(path)
    print("Excel loaded")
    return excel_data