from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[2]
df = pd.read_csv(BASE_DIR / "outputs" / "final_merged_dataset.csv")

def create_visuals(df):

#total cost over time
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    df["total_cost"] = df["quantity_mt"] * df["price_per_mt"]

# Group by date
    cost_trend = df.groupby("date")["total_cost"].sum()

    plt.figure(figsize=(12, 6))

    cost_trend.plot(
    kind="line",
    linewidth=2,
    marker="o",
    markersize=4
    )

    plt.title("Total Fuel Cost Over Time", fontsize=14, fontweight="bold")
    plt.xlabel("Date", fontsize=11)
    plt.ylabel("Total Cost", fontsize=11)

    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig("outputs/cost_over_time.png", dpi=300)
    plt.close()


#Fuel by port
    #df.groupby("date")["total_cost"].sum().plot()
    #df.groupby("date")["quantity_mt"].sum().plot(kind="bar")
    #plt.title("Total Fuel Cost Over Time")
    #plt.savefig("outputs/fuel_by_port.png")
    #plt.close()

    plt.figure(figsize=(10,6))
    fuel_by_port = df.groupby("port")["quantity_mt"].sum().sort_values(ascending=False)
    fuel_by_port.plot(kind="bar")

    plt.title("Fuel Consumption by Port")
    plt.xlabel("Port")
    plt.ylabel("Fuel Quantity(mt)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("outputs/fuel_by_port.png")
    plt.close()

#Fuel type distribution
    df.groupby("fuel_type")["quantity_mt"].sum().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Fuel Type Distribution")
    plt.ylabel("")              #removes unnecessary quantity_mt label on the left
    plt.savefig("outputs/fuel_type.png")
    plt.close()

#monthly fuel consumption trend
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)

    monthly_fuel = df.groupby(df["date"].dt.to_period("M"))["quantity_mt"].sum()
    monthly_fuel.index = monthly_fuel.index.astype(str)

    plt.figure()
    monthly_fuel.plot(marker="o")
    plt.title("Monthly Fuel Consumption Trend")
    plt.xlabel("Month")
    plt.ylabel("Fuel Quantity (MT)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/monthly_fuel_trend.png")
    plt.close()

#price trend over time
    # Average fuel price trend over time
    price_trend = df.groupby(df["date"])["price_per_mt"].mean()

    plt.figure()
    price_trend.plot()
    plt.title("Fuel Price Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Average Price per MT")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/price_trend.png")
    plt.close()

#Cost vs Quantity Trend
    # Cost vs Quantity trend over time
    daily_trend = df.groupby(df["date"])[["total_cost", "quantity_mt"]].sum()

    plt.figure()
    daily_trend.plot()
    plt.title("Cost vs Quantity Trend Over Time")
    plt.xlabel("Date")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/cost_vs_quantity_trend.png")
    plt.close()


#correlation heatmap between quantity, price and total cost

    #correlation matrix
    corr = df[["quantity_mt", "price_per_mt", "total_cost"]].corr()

    plt.figure(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Between Key Variables")
    plt.tight_layout()
    plt.savefig("outputs/correlation_heatmap.png")
    plt.close()

    #scatter plot--price vs quantity
    plt.figure()

    plt.scatter(df["price_per_mt"], df["quantity_mt"], alpha=0.6)

    plt.title("Correlation: Price vs Quantity")
    plt.xlabel("Price per MT")
    plt.ylabel("Quantity (MT)")
    plt.tight_layout()

    plt.savefig("outputs/price_vs_quantity_scatter.png")
    plt.close()

    #scatter plot---cost vs quantity
    plt.scatter(df["quantity_mt"], df["total_cost"], alpha=0.6)

    plt.title("Correlation: Quantity vs Total Cost")
    plt.xlabel("Quantity (MT)")
    plt.ylabel("Total Cost")
    plt.tight_layout()

    plt.savefig("outputs/quantity_vs_cost_scatter.png")
    plt.close()




