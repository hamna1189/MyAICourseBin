import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

df = pd.read_csv(
    r"C:\Users\user\Documents\GitHub\FULL-STACK-B-8-Wed-Thru-Fri\FinalAssessment\Starlink & SpaceX Data Dataset\spacex_launches.csv"
)

df["date_utc"] = pd.to_datetime(df["date_utc"], errors="coerce")
df["year"] = df["date_utc"].dt.year
df["month"] = df["date_utc"].dt.month
df = df.drop(columns=["date_utc", "details"], errors="ignore")
df = df.fillna("Unknown")

encoder = LabelEncoder()

for col in df.columns:
    if not pd.api.types.is_numeric_dtype(df[col]):
        df[col] = encoder.fit_transform(df[col].astype(str))

X = df.drop("success", axis=1)
y = df["success"].astype(int)

# Scale data
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Reshape for LSTM
X = X.reshape((X.shape[0], 1, X.shape[1]))

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# LSTM Model
model = Sequential()
model.add(LSTM(50, input_shape=(1, X.shape[2])))
model.add(Dense(1, activation="sigmoid"))

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train
model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=8,
    validation_data=(X_test, y_test),
    verbose=1
)

# Predict
pred = model.predict(X_test)
pred = (pred > 0.5).astype(int)

# Accuracy
print("Accuracy:", accuracy_score(y_test, pred))