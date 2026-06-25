import pandas as pd

df = pd.read_csv(
    "New folder/archive (1)/AirQuality.csv",
    sep=";",
    decimal=","
)

# Remove empty columns
df = df.drop(columns=["Unnamed: 15", "Unnamed: 16"])

# Remove missing rows
df = df.dropna()

print(df.shape)
print(df.head())