import pandas as pd

def calculate_kpis(df):
    df["total_cost"] = df ["quantity_mt"] * df["price_per_mt"]

    total_cost = df["total_cost"].sum()
    total_quantity = df["quantity_mt"].sum()
    avg_price = df["price_per_mt"]. mean()
    cost_efficiency = total_cost / total_quantity

    cheapest_port = df.groupby("port")["price_per_mt"].mean().idxmin()
    most_used_fuel = df.groupby("fuel_type")["quantity_mt"].sum().idxmax()

    kpis = {
        "Total Fuel Cost" : total_cost,
        "Total Fuel Quantity": total_quantity,
        "Average Price": avg_price,
        "Cost Efficiency": cost_efficiency,
        "Cheapest Port": cheapest_port,
        "Most Used Fuel": most_used_fuel
    }

    return kpis