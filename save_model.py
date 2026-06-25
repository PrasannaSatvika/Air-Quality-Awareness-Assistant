import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv(
    "New folder/archive (1)/AirQuality.csv",
    sep=";",
    decimal=","
)

df = df.drop(columns=["Unnamed: 15", "Unnamed: 16"])
df = df.replace(-200, pd.NA)
df = df.dropna()

def air_quality_category(co):
    if co <= 2:
        return "Good"
    elif co <= 5:
        return "Moderate"
    else:
        return "Poor"

df["Air_Quality"] = df["CO(GT)"].apply(air_quality_category)

X = df[
[
    "PT08.S1(CO)",
    "NMHC(GT)",
    "C6H6(GT)",
    "PT08.S2(NMHC)",
    "NOx(GT)",
    "PT08.S3(NOx)",
    "NO2(GT)",
    "PT08.S4(NO2)",
    "PT08.S5(O3)",
    "T",
    "RH",
    "AH"
]
]

y = df["Air_Quality"]

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "air_quality_model.pkl")

print("Model Saved Successfully!")