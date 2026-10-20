import os
import numpy as np
import pandas as pd

print(" Generando dataset analítico avanzado para Kalista...")

np.random.seed(42)
n_records = 500

data = {
    "Match_ID": [f"Match_{i}" for i in range(n_records)],
    # Tier dividido entre Pro Play y SoloQueue Bajos
    "Tier": np.random.choice(
        ["Hierro-Oro (SoloQueue)", "Challenger / Pro Play"],
        size=n_records,
        p=[0.6, 0.4],
    ),
    "Gamelength": np.random.randint(1500, 2600, size=n_records),
}

df = pd.DataFrame(data)

df["Win"] = df.apply(
    lambda row: np.random.choice(
        [0, 1], p=[0.548, 0.452]
        if row["Tier"] == "Hierro-Oro (SoloQueue)"
        else [0.452, 0.548]
    ),
    axis=1,
)

df["Gold_Diff_15"] = df.apply(
    lambda row: np.random.normal(318.5, 120)
    if row["Tier"] == "Challenger / Pro Play"
    else np.random.normal(-210, 150),
    axis=1,
)
df["CS_Diff_15"] = df.apply(
    lambda row: np.random.normal(3.0, 1.2)
    if row["Tier"] == "Challenger / Pro Play"
    else np.random.normal(-2.5, 1.5),
    axis=1,
)

df["R_Effectiveness"] = df.apply(
    lambda row: np.random.uniform(60, 95)
    if row["Tier"] == "Challenger / Pro Play"
    else np.random.uniform(30, 60),
    axis=1,
)

df["DPS_Efficiency_Score"] = df.apply(
    lambda row: np.random.uniform(80, 100)
    if row["Tier"] == "Challenger / Pro Play"
    else np.random.uniform(40, 75),
    axis=1,
)

df["Ban_Rate"] = df.apply(
    lambda row: 65.0
    if row["Tier"] == "Challenger / Pro Play"
    else 1.8,
    axis=1,
)

os.makedirs("data/processed", exist_ok=True)
output_path = "data/processed/kalista_analytics_dataset.csv"
df.to_csv(output_path, index=False)

print(f"✅ ¡Dataset analítico avanzado guardado en: {output_path}!")
print(df.groupby("Tier")[["Win", "Gold_Diff_15", "R_Effectiveness"]].mean())