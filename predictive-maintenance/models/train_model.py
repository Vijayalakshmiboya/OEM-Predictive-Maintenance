
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load historical data
data = pd.read_csv("data/historical_data.csv")

# Train an anomaly detection model
features = ["temperature", "vibration", "pressure"]
X = data[features]

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X)

# Save the model
joblib.dump(model, "models/anomaly_model.pkl")
print("Model saved to models/anomaly_model.pkl")
