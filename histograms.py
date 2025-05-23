
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/agriculture_mock_data.csv")
os.makedirs("visuals", exist_ok=True)

for col in df.columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.savefig(f"visuals/hist_{col}.png")
    plt.close()
