
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# STEP 1: Load dataset from online source
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

print("Online Dataset:")
print(df.head())

# STEP 2: Create our own DataFrame
data = {
    "Hours_Study": [2, 3, 4, 5, 6, 7, 8, 9, 3, 6, 8, 10],
    "Hours_Sleep": [5, 6, 6, 7, 7, 8, 8, 9, 7, 8, 6, 8],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95, 70, 85, 90, 98],
    "Marks": [30, 38, 45, 55, 65, 75, 85, 95, 42, 72, 82, 98]
}

df2 = pd.DataFrame(data)

print("\nOur Own DataFrame:")
print(df2)

# STEP 3: Select input and output
X = df2[["Hours_Study", "Hours_Sleep", "Attendance"]]
y = df2["Marks"]

# STEP 4: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# STEP 5: Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# STEP 6: Predict test data
predictions = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(predictions.round(2))

# STEP 7: Check model accuracy
print("\nR2 Score:", round(r2_score(y_test, predictions), 2))

# STEP 8: Check learned coefficients
print("\nModel Coefficients:")
print("Study Hours:", round(model.coef_[0], 2))
print("Sleep Hours:", round(model.coef_[1], 2))
print("Attendance:", round(model.coef_[2], 2))
print("Intercept:", round(model.intercept_, 2))

# STEP 9: Predict marks for a new student
new_student = pd.DataFrame({
    "Hours_Study": [6],
    "Hours_Sleep": [8],
    "Attendance": [85]
})

result = model.predict(new_student)

print("\nNew Student Details:")
print(new_student)

print("\nPredicted Student Marks:", round(result[0], 2))
