import os
import joblib
import pandas as pd

model = None

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "model.pkl")

def get_model():
    global model
    if model is None:
        if not os.path.exists(MODEL_PATH):
            raise RuntimeError("model.pkl not found. Run train.py first.")
        model = joblib.load(MODEL_PATH)
    return model

def predict_price(data: dict):
    model = get_model()
    df = pd.DataFrame([data])
    return float(model.predict(df)[0])