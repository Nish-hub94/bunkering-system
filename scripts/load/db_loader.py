import pandas as pd
from sqlalchemy import create_engine


def load_to_db(df, table_name, connection_string):


    connection = create_engine(connection_string)
    df.to_sql(table_name, connection, if_exists="replace", index=False)
    print(f"Loaded Dataframe into table '{table_name}' ")

