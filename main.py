from scripts.extract.csv_loader import load_csv
from scripts.extract.excel_loader import load_excel
from scripts.extract.api_loader import load_api
from scripts.extract.sql_loader import load_sql
from scripts.transform import clean_dataframe
from scripts.load import load_to_db
import pandas as pd
from scripts.analytics.kpis import calculate_kpis
import matplotlib.pyplot as plt
from scripts.analytics.visualizations import  create_visuals
from scripts.analytics.benchmarking import run_benchmarking
import os

#..API url....
url = "http://127.0.0.1:5000/fuel_prices"

#..DB connection to raw data...
connection_string="mysql+pymysql://root:letMEin2331!@127.0.0.1:3306/bunkering_management"

#..DB connection to new db
connection_string_dw = "mysql+pymysql://root:letMEin2331!@127.0.0.1:3306/cleaned_bunkering_dw"

#....Loading  the raw data.....
df_csv = load_csv("data/fuel_deliveries.csv")
df_excel = load_excel("data/vessel_logs.xlsx")

if os.getenv("CI") != "true":
    df_api = load_api(url)
else:
    df_api =pd.DataFrame()


#...sql data...
sql_data= load_sql(connection_string)

#..cleaning data...
df_csv = clean_dataframe(df_csv)
df_excel = clean_dataframe(df_excel)
df_api = clean_dataframe(df_api)

#..clean SQL..
df_ports = clean_dataframe(sql_data["ports"])
df_suppliers = clean_dataframe(sql_data["suppliers"])
df_fuel_prices = clean_dataframe(sql_data["fuel_prices"])

#..Creating the star schema..

#DIM PORTS
dim_ports = df_ports.copy()

#DIM FUEL
#dim_fuel = df_fuel_prices[["fuel_type", "price"]].drop_duplicates()
dim_fuel = df_fuel_prices[["fuel_type", "price"]]
dim_fuel = dim_fuel.groupby("fuel_type", as_index=False).agg({
    "price" : "max"
})

#DIM VESSEL
#dim_vessel = df_excel[["vessel_name", "capacity_teu"]].drop_duplicates()
dim_vessel = df_excel[["vessel_name", "capacity_teu"]]
dim_vessel = dim_vessel.groupby("vessel_name", as_index=False).agg({
    "capacity_teu": "max",
})

#DIM DATE
#df_fuel_prices["date"] = pd.to_datetime(df_fuel_prices["date"])
df_fuel_prices["date"] = pd.to_datetime(df_fuel_prices["date"])

date_range = pd.date_range(
    start = df_fuel_prices["date"].min(),
    end = df_fuel_prices["date"].max()

)
#dim_date = pd.DataFrame()
dim_date = pd.DataFrame({"date":date_range})
dim_date["date"] = df_fuel_prices["date"]
dim_date["year"] = df_fuel_prices["date"].dt.year
dim_date["month"] = df_fuel_prices["date"].dt.month
dim_date["day"] = df_fuel_prices["date"].dt.day

dim_date = dim_date.drop_duplicates()



#FACT TABLE
fact_bunkering = df_csv.copy()

print("Star Schema created")

#..loading schema tables to the database
load_to_db(fact_bunkering, "fact_bunkering", connection_string_dw)

load_to_db(dim_ports, "dim_ports", connection_string_dw)
load_to_db(dim_fuel, "dim_fuel", connection_string_dw)
load_to_db(dim_vessel, "dim_vessel", connection_string_dw)
load_to_db(dim_date, "dim_date", connection_string_dw)

#...loading to raw data to database...
load_to_db(df_csv, "fuel_deliveries", connection_string)
load_to_db(df_excel, "vessel_info", connection_string)
load_to_db(df_api, "fuel_prices", connection_string)

#loading cleaned data into database
load_to_db(df_csv, "cleaned_fuel_deliveries", connection_string)
load_to_db(df_excel, "cleaned_vessel_info", connection_string)
load_to_db(df_api, "cleaned_fuel_prices", connection_string)
load_to_db(df_suppliers, "cleaned_suppliers", connection_string)
load_to_db(df_ports, "cleaned_ports", connection_string)


print("Suppliers columns:", df_suppliers.columns)
print("Ports columns:", df_ports.columns)
print("Fuel Prices columns:", df_fuel_prices.columns)
print("Vessel info columns:", df_excel.columns)
print("Fuel deliveries columns:", df_csv.columns)

#merging the cleaned SQL tables
#merged_sql = df_suppliers.merge(df_ports, left_on="port_id",right_on="port_id", how="left")
merged_sql = df_fuel_prices.merge(df_ports, left_on="port",right_on="port_name", how="left")

print("SQL tables merged successfully")
print(merged_sql.head())

#save merged SQL table

#save  merged SQL table
merged_sql.to_csv("data/merge_sql.csv", index=False)

#save other cleaned data sources
df_csv.to_csv("data/fuel_deliveries_cleaned.csv", index=False)
df_excel.to_csv("data/vessel_logs_cleaned.csv", index=False)
df_api.to_csv("data/cleaned_fuel_prices.csv", index=False)

df_suppliers.to_csv("data/cleaned_suppliers.csv", index=False)

print("All cleaned and merged CSVS exported for Power BI")


df = fact_bunkering.copy()
print(df.columns)

#merging with port
df_ports = df_ports.drop_duplicates(subset="port_name")
df =df.merge(df_ports, left_on="port", right_on="port_name", how="left")
print(df.columns)

df.drop(columns =["port_name"], inplace = True)
print(df.columns)

#merging with suppliers
print(df_suppliers.columns)
df_suppliers = df_suppliers.drop_duplicates(subset="supplier_name")
df =df.merge(df_suppliers, left_on="supplier",right_on="supplier_name", how="left")
print(df.columns)

df.drop(columns=["supplier_name"], inplace =True)
print(df.columns)

#validating the merged dataset
print(df.isnull().sum())
print(len(df))

#saving the final dataset
df.to_csv("outputs/final_merged_dataset.csv", index=False)

#saving the KPIs to file
kpis= calculate_kpis(df_csv)

#saving to text file
with open ("outputs/kpis.txt", "w") as kpis_file:
    for key, value in kpis.items():
        kpis_file.write(f"{key}: {value}\n")

print("KPIS saved")

#calling visualisations
create_visuals(df_csv)
print("Charts created successfully")

#calling benchmarking
run_benchmarking(df_csv)
print("Benchmarking completed")


def run_pipeline():
    print("Pipeline Started")

    url = "http://127.0.0.1:5000/fuel_prices"

    df_csv = load_csv("data/fuel_deliveries.csv")
    df_excel = load_excel("data/vessel_logs.xlsx")
    df_api = load_api(url)

    print("All data loaded successfully")


if __name__ == "__main__":
    run_pipeline()
