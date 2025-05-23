from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("models/yield_model.pkl")

# InputData
class InputData(BaseModel):
    temperature: float
    rainfall: float
    soil_ph: float
    fertilizer_amount: float

@app.post("/predict")
def predict(data: InputData):
    features = np.array([[data.temperature, data.rainfall, data.soil_ph, data.fertilizer_amount]])
    prediction = model.predict(features)
    return {"predicted_yield": prediction[0]}
