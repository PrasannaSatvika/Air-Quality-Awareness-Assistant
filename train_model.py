import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv(
    "New folder/archive (1)/AirQuality.csv",
    sep=";",
    decimal=","
)

# Remove unwanted columns
df = df.drop(columns=["Unnamed: 15", "Unnamed: 16"])

# Replace invalid values (-200) with missing values
df = df.replace(-200, pd.NA)

# Drop missing values
df = df.dropna()

# Create Air Quality Category
def air_quality_category(co):
    if co <= 2:
        return "Good"
    elif co <= 5:
        return "Moderate"
    else:
        return "Poor"

df["Air_Quality"] = df["CO(GT)"].apply(air_quality_category)

# Features
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

# Target
y = df["Air_Quality"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Random Forest Model
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", round(accuracy * 100, 2), "%")