import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
# STEP 1 - CREATE DATA
data = pd.DataFrame({
    "Hours_Studied": [1, 2, 2, 3, 3, 4, 4, 5, 5, 6,6, 7, 7, 8, 8, 9, 9, 10, 10, 11],
    "Attendance": [50, 55, 60, 58, 65, 62, 70, 68, 75, 72,80, 78, 85, 82, 88, 86, 92, 90, 95, 98],
    "Result": [0, 0, 0, 0, 0, 0, 0, 1, 0, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})
print(data)

# STEP 2 - SEPARATE FEATURES AND TARGET
X = data[["Hours_Studied", "Attendance"]]
y = data["Result"]

# STEP 3 - SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# STEP 4 - SCALE DATA
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# STEP 5 - CREATE KNN MODEL
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# STEP 6 - MAKE PREDICTIONS
y_pred = model.predict(X_test)
print("Actual:", y_test.values)
print("Predicted:", y_pred)

# STEP 7 - CHECK MODEL PERFORMANCE
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print("\nAccuracy:", round(accuracy, 3))
print("Precision:", round(precision, 3))
print("Recall:", round(recall, 3))
print("F1 Score:", round(f1, 3))

# STEP 8 - CONFUSION MATRIX
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# STEP 9 - TEST DIFFERENT K VALUES
k_values = range(1, 16)
accuracy_values = []
for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_values.append(accuracy)
    print("K =", k, "Accuracy =", round(accuracy, 3))

# STEP 10 - GRAPH K VS ACCURACY
plt.plot(k_values, accuracy_values, marker="o")
plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy for Different K Values")
plt.xticks(list(k_values))
plt.grid()
plt.show()

# STEP 11 - KNN DECISION BOUNDARY
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
x_min = X_train[:, 0].min() - 1
x_max = X_train[:, 0].max() + 1
y_min = X_train[:, 1].min() - 1
y_max = X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),np.linspace(y_min, y_max, 200))
points = np.c_[xx.ravel(), yy.ravel()]
prediction = model.predict(points)
prediction = prediction.reshape(xx.shape)
plt.contourf(xx, yy, prediction, alpha=0.3)
plt.scatter(
    X_train[:, 0],
    X_train[:, 1],
    c=y_train,
    edgecolors="black"
)
plt.xlabel("Hours Studied")
plt.ylabel("Attendance")
plt.title("KNN Decision Boundary - K = 5")
plt.show()

# STEP 12 - COMPARE DIFFERENT K VALUES
k_values = [1, 3, 5, 7]
for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("K =", k, "Accuracy =", round(accuracy, 3))