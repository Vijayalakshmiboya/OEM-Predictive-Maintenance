
import pandas as pd
import numpy as np
import time

# Simulate IoT sensor data
def generate_data(num_records=1000):
    data = {
        "timestamp": pd.date_range(start="2024-01-01", periods=num_records, freq="H"),
        "temperature": np.random.normal(50, 5, num_records),
        "vibration": np.random.normal(3, 0.5, num_records),
        "pressure": np.random.normal(100, 10, num_records),
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_data()
    df.to_csv("data/simulated_data.csv", index=False)
    print("Simulated data saved to data/simulated_data.csv")
