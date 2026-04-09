def clean_dataframe(df):
    if df is not None:
        df = df.dropna()

    return df