import json
import joblib

def save_metrics(metrics: dict, path="outputs/metrics.json"):
    with open(path, "w") as f:
        json.dump(metrics, f, indent=4)
    print("✅ Metrics saved successfully.")

def load_model(path="outputs/LinearModel.joblib"):
    return joblib.load(path)
