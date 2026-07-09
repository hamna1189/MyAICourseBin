import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns  

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

#file read 
df = pd.read_csv("C:\\Users\\user\\Documents\\GitHub\\FULL-STACK-B-8-Wed-Thru-Fri\\FinalAssessment\\Space Industry Analytics")
print("First 5 records")
print("\nDataset shape:", df.shape)
print("\nNull values")
print(df.isnull().sum())
print("\nDescription")
print(df.describe())
plt.figure(figsize=(7,5))
sns.scatterplot ( 
    data=df,
    x='Budget',
    y='Revenue'
)
plt.title("Budget vs Revenue")
plt.show()
plt.figure(figsize=(8,6))
sns.heatmap ( 
    df.corr(numeric_only=True),
    annot=True
)
plt.show()
x = df[['Budget']]
y = df['Revenue']
x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=1
)
lr = LinearRegression()
lr.fit(x_train, y_train)
pred = lr.predict(x_test)
print("\nActual Values")
print(y_test.values)
print("\nPredicted Values")
print(pred)
print("\nMAE:",
     mean_absolute_error(y_test, pred))

print("R2 Score:",
            r2_score(y_test, pred))
plt.figure(figsize=(7,5))
plt.scatter(y_test, pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted Revenue")
plt.show() 