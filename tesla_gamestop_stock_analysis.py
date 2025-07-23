# Tesla and GameStop Stock Analysis using Python with Sample Data

# Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# -----------------------------
# Utility: Create sample stock data
# -----------------------------

def create_sample_stock_data():
    dates = pd.date_range(start="2020-01-01", periods=10, freq='ME')
    data = {
        'Date': dates,
        'Open': [100 + i*5 for i in range(10)],
        'High': [105 + i*5 for i in range(10)],
        'Low': [95 + i*5 for i in range(10)],
        'Close': [102 + i*5 for i in range(10)],
        'Volume': [1000000 + i*10000 for i in range(10)]
    }
    return pd.DataFrame(data)


def create_sample_revenue_data():
    dates = pd.date_range(start="2020-01-01", periods=10, freq='QE')
    data = {
        'Date': dates,
        'Revenue': [round(5 + i * 0.5, 2) for i in range(10)]  # in billions
    }
    return pd.DataFrame(data)
# -----------------------------
# Tesla Stock Data
# -----------------------------

tesla_data = create_sample_stock_data()
print("Tesla Stock Data (First 5 Rows):")
print(tesla_data.head())
# -----------------------------
# Tesla Revenue Data
# -----------------------------

tesla_revenue = create_sample_revenue_data()
print("\nTesla Revenue Data (Last 5 Rows):")
print(tesla_revenue.tail())
# -----------------------------
# GameStop Stock Data
# -----------------------------

gme_data = create_sample_stock_data()
print("\nGameStop Stock Data (First 5 Rows):")
print(gme_data.head())
# -----------------------------
# GameStop Revenue Data
# -----------------------------

gme_revenue = create_sample_revenue_data()
print("\nGameStop Revenue Data (Last 5 Rows):")
print(gme_revenue.tail())
# -----------------------------
# Plot Tesla Stock Graph
# -----------------------------

def make_graph(data, title):
    plt.figure(figsize=(14,6))
    plt.plot(data['Date'], data['Close'], marker='o')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

make_graph(tesla_data, "Tesla Stock Price Over Time")
# -----------------------------
# Plot GameStop Stock Graph
# -----------------------------

make_graph(gme_data, "GameStop Stock Price Over Time")
