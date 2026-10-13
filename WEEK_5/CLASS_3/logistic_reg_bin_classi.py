
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# STEP 1: Load dataset from online source
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

print("Online Dataset:")
print(df.head())

# STEP 2: Create our own DataFrame
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 4, 6, 9, 3, 7, 8, 5],
    "Attendance": [40, 45, 50, 55, 60, 65, 70, 90, 50, 60, 75, 95, 45, 80, 85, 70],
    "Previous_Marks": [20, 25, 35, 40, 45, 55, 65, 85, 30, 45, 60, 95, 25, 75, 80, 50],
    "Pass": [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1]
}

df2 = pd.DataFrame(data)

print("\nOur Own Dataset:")
print(df2)

# STEP 3: Select input and output
X = df2[["Study_Hours", "Attendance", "Previous_Marks"]]
y = df2["Pass"]

# STEP 4: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# STEP 5: Create and train model
model = LogisticRegression()
model.fit(X_train, y_train)

# STEP 6: Make predictions
predictions = model.predict(X_test)

print("\nActual Results:")
print(y_test.values)

print("\nPredicted Results:")
print(predictions)

# STEP 7: Check model performance
print("\nAccuracy:", accuracy_score(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# STEP 8: Predict a new student's result
new_student = pd.DataFrame({
    "Study_Hours": [6],
    "Attendance": [80],
    "Previous_Marks": [65]
})

result = model.predict(new_student)
probability = model.predict_proba(new_student)

print("\nNew Student Details:")
print(new_student)

print("\nPredicted Result:", "Pass" if result[0] == 1 else "Fail")
print("Probability of Fail:", round(probability[0][0] * 100, 2), "%")
print("Probability of Pass:", round(probability[0][1] * 100, 2), "%")
