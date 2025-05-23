import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Carrega dados
data = pd.read_csv("data/agriculture_mock_data.csv")
X = data.drop(columns=["yield"])
y = data["yield"]

# Divide dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treina modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avalia modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"MSE: {mse}")

# Salva modelo
joblib.dump(model, "models/yield_model.pkl")

import mlflow
mlflow.set_experiment("Agriculture Yield Prediction")

with mlflow.start_run():
    mlflow.log_param("model_type", "RandomForestRegressor")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("mse", mse)
    mlflow.sklearn.log_model(model, "model")
