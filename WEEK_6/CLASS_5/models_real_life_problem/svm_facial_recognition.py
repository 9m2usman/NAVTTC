# ============================================================
# SVM - Facial recognition (Olivetti faces, fetched automatically)
# 400 images, 40 different people, 10 photos each
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

# ---------- E: EXTRACT ----------
faces = fetch_olivetti_faces(shuffle=True, random_state=42)
X = faces.data          # each row = one 64x64 image flattened to 4096 pixel values
y = faces.target        # person id 0..39
print("X shape:", X.shape, "| people:", len(np.unique(y)))

# ---------- T: TRANSFORM ----------
print("Missing values:", np.isnan(X).sum())   # images have no missing pixels

# Show some faces
fig, ax = plt.subplots(2, 6, figsize=(14, 5))
for i, a in enumerate(ax.ravel()):
    a.imshow(X[i].reshape(64, 64), cmap="gray")
    a.set_title(f"Person {y[i]}")
    a.axis("off")
plt.suptitle("Sample faces")
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

# ---------- SCALING + MODEL in one pipeline ----------
# SVM is distance based, so scaling is compulsory.
pipe = Pipeline([ ("scaler", StandardScaler()),("svm", SVC()) ])

# Try different kernels and C values (C = how strict the margin is)
param_grid = {"svm__kernel": ["linear", "rbf"],"svm__C": [0.1, 1, 10, 100],}
grid = GridSearchCV(pipe, param_grid, cv=5, n_jobs=-1)
grid.fit(X_train, y_train)

print("Best params:", grid.best_params_)
print("Best CV accuracy:", round(grid.best_score_, 4))

model = grid.best_estimator_
pred = model.predict(X_test)

# ---------- Metrics ----------
print("Test accuracy:", round(accuracy_score(y_test, pred), 4))
print("Macro F1     :", round(f1_score(y_test, pred, average="macro"), 4))

# ---------- Graphs ----------
# 1) Grid search results: accuracy for each kernel and C
res = pd.DataFrame(grid.cv_results_)
res["kernel"] = res["param_svm__kernel"]
res["C"] = res["param_svm__C"].astype(float)
for k in res["kernel"].unique():
    sub = res[res["kernel"] == k]
    plt.plot(sub["C"], sub["mean_test_score"], marker="o", label=k)
plt.xscale("log")
plt.xlabel("C"); plt.ylabel("CV accuracy")
plt.title("SVM kernel and C comparison")
plt.legend()
plt.show()

# 2) Confusion matrix (40 x 40)
plt.figure(figsize=(10, 8))
sns.heatmap(confusion_matrix(y_test, pred), cmap="Blues")
plt.title("Confusion matrix (40 people)")
plt.xlabel("Predicted person"); plt.ylabel("Actual person")
plt.show()

# 3) Show wrongly predicted faces
wrong = np.where(pred != y_test)[0][:6]
if len(wrong) > 0:
    fig, ax = plt.subplots(1, len(wrong), figsize=(3 * len(wrong), 3.5))
    ax = np.atleast_1d(ax)
    for a, i in zip(ax, wrong):
        a.imshow(X_test[i].reshape(64, 64), cmap="gray")
        a.set_title(f"True {y_test[i]}\nPred {pred[i]}")
        a.axis("off")
    plt.suptitle("Mistakes")
    plt.show()
else:
    print("No mistakes on the test set!")