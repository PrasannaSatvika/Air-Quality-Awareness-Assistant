import pandas as pd

df = pd.read_csv(
    "New folder/archive (1)/AirQuality.csv",
    sep=";",
    decimal=","
)

df = df.drop(columns=["Unnamed: 15", "Unnamed: 16"])
df = df.dropna()

def air_quality_category(co):
    if co <= 2:
        return "Good"
    elif co <= 5:
        return "Moderate"
    else:
        return "Poor"

df["Air_Quality"] = df["CO(GT)"].apply(air_quality_category)

print(df[["CO(GT)", "Air_Quality"]].head())