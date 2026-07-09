import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Dataset
df = pd.read_csv(r"C:\\Users\\user\\Documents\\GitHub\\FULL-STACK-B-8-Wed-Thru-Fri\\FinalAssessment\\SpaceX Missions, 2006-Present\\database.csv")

print(df.columns)
print(df.head())
print(df.info())
print(df.describe(include="all"))
print(df.isnull().sum())

df = df.fillna("Unknown")
le = LabelEncoder()

for col in df.columns:
    try:
        pd.to_numeric(df[col])
    except:
        df[col] = le.fit_transform(df[col].astype(str))

print(df.dtypes)
numeric_df = df.select_dtypes(include=["number"])
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

sns.countplot(x=df["Mission Outcome"])
plt.xticks(rotation=45)
plt.show()

X = df.drop("Mission Outcome", axis=1)
y = df["Mission Outcome"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)
print("Accuracy:", acc)

cm = confusion_matrix(y_test, pred)
print(cm)

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Classification Report
print(classification_report(y_test, pred))