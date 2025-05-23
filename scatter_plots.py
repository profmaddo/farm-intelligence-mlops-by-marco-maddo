
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/agriculture_mock_data.csv")
os.makedirs("visuals", exist_ok=True)

pairs = [("temperature", "yield"), ("rainfall", "yield"),
         ("soil_ph", "yield"), ("fertilizer_amount", "yield")]

for x, y in pairs:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df[x], y=df[y])
    plt.title(f"{x.capitalize()} vs {y.capitalize()}")
    plt.xlabel(x.capitalize())
    plt.ylabel(y.capitalize())
    plt.savefig(f"visuals/scatter_{x}_vs_{y}.png")
    plt.close()
