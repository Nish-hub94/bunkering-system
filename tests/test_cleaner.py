import pandas as pd
from scripts.transform.cleaner import clean_dataframe

def test_clean_dataframe():
    df = pd.DataFrame({
        "A":[1, None, 3],
        "B": [4, 5, None]
    })

    cleaned = clean_dataframe(df)

    assert cleaned.isnull().sum().sum() == 0