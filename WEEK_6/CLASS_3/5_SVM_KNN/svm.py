import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
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

# STEP 5 - CREATE SVM MODEL
model = SVC(kernel="linear", C=1)
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

# STEP 9 - TEST DIFFERENT C VALUES
c_values = [0.01, 0.1, 1, 10, 100]
for c in c_values:
    model = SVC(kernel="linear", C=c)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("C =", c, "Accuracy =", round(accuracy, 3))

# STEP 10 - COMPARE KERNELS
kernels = ["linear", "rbf", "poly"]
for kernel in kernels:
    model = SVC(kernel=kernel, C=1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Kernel =", kernel, "Accuracy =", round(accuracy, 3))

# STEP 11 - VISUALIZE SVM DECISION BOUNDARY
model = SVC(kernel="linear", C=1)
model.fit(X_train, y_train)
x_min = X_train[:, 0].min() - 1
x_max = X_train[:, 0].max() + 1
y_min = X_train[:, 1].min() - 1
y_max = X_train[:, 1].max() + 1
xx, yy = np.meshgrid( np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200) )
points = np.c_[xx.ravel(), yy.ravel()]
prediction = model.predict(points)
prediction = prediction.reshape(xx.shape)
plt.contourf(xx, yy, prediction, alpha=0.3)
plt.scatter( X_train[:, 0], X_train[:, 1], c=y_train, edgecolors="black" )
plt.xlabel("Hours Studied")
plt.ylabel("Attendance")
plt.title("SVM Decision Boundary")
plt.show()