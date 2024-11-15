
from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/anomaly_model.pkl")

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    predictions = model.predict(df)
    df["anomaly"] = predictions
    anomalies = df[df["anomaly"] == -1]
    return jsonify(anomalies.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
