#creat_engine function is used to connect python to db

from sqlalchemy import create_engine
import pandas as pd

def load_sql(connection_string):
    connection = create_engine(connection_string)

    #"mysql+pymysql://root:letMEin2331!@127.0.0.1:3306/bunkering_management"

    df_ports =pd.read_sql("SELECT * FROM ports", connection)
    df_suppliers =pd.read_sql("SELECT * FROM suppliers", connection)
    df_fuel_prices=pd.read_sql("SELECT * FROM fuel_prices", connection)

    print("SQL data loaded")

    return{
        "ports": df_ports,
        "suppliers": df_suppliers,
        "fuel_prices": df_fuel_prices
    }


