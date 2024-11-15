
# Predictive Maintenance Prototype

This project demonstrates a basic prototype for implementing predictive maintenance using machine learning models and IoT data.

## Features
- Simulates IoT sensor data for equipment monitoring.
- Trains an anomaly detection model using historical data.
- Provides a web-based dashboard for monitoring system health and visualizing anomalies.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Simulate Data:
   ```bash
   python scripts/data_simulator.py
   ```

3. Train the Model:
   ```bash
   python models/train_model.py
   ```

4. Run the Dashboard:
   ```bash
   python app/app.py
   ```

## Folder Structure
- **data/**: Contains simulated and historical data files.
- **models/**: Includes training scripts and the trained model.
- **app/**: Flask application with templates and static files.
- **scripts/**: Helper scripts for data simulation and preprocessing.

## License
MIT
