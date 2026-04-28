import matplotlib.pyplot as plt
from openpyxl.styles.builtins import percent


def run_benchmarking(df):
    # Internal benchmark = average price across all ports
    benchmark_price = df["price_per_mt"].mean()

    # Average price by port
    port_prices = df.groupby("port")["price_per_mt"].mean().sort_values()

    # Save benchmark text report
    with open("outputs/benchmarking.txt", "w") as f:
        f.write(f"Overall Benchmark Price: {benchmark_price:.2f}\n\n")

        for port, price in port_prices.items():

            diff = price - benchmark_price
            percent = (diff / benchmark_price) * 100

            if diff > 0:
                status = "Above Benchmark"
            else:
                status = "Below Benchmark"

            f.write(
                f"{port}: {price:.2f} | {status} ({percent:.2f}%)\n"
            )

    # Create chart
    plt.figure(figsize=(10, 6))

    port_prices.plot(kind="bar")

    plt.axhline(
        benchmark_price,
        color="red",
        linestyle="--",
        label="Benchmark Average"
    )

    plt.title("Port Fuel Price Benchmarking")
    plt.xlabel("Port")
    plt.ylabel("Average Price per MT")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()

    plt.savefig("outputs/port_benchmark.png")
    plt.close()

