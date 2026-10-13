# ============================================================
# RANDOM FOREST - Credit Card Fraud Detection (OpenML API)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    precision_recall_curve,
    average_precision_score
)

# ---------- E: EXTRACT ----------
data = fetch_openml(data_id=1597, as_frame=True)
df = data.frame

# Clean column names
df.columns = df.columns.astype(str).str.strip()

df["Class"] = pd.to_numeric(df["Class"]).astype(int)

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df["Class"].value_counts())

# ---------- T: TRANSFORM ----------
df = df.drop_duplicates().dropna().copy()

# Keep all fraud rows and sample normal transactions
fraud = df[df["Class"] == 1]
normal = df[df["Class"] == 0].sample(n=100000, random_state=42)

df = pd.concat([fraud, normal]).sample(frac=1, random_state=42).copy()

print("\nShape after sampling:", df.shape)

sns.countplot(x="Class", data=df)
plt.title("Fraud (1) vs Normal (0) After Sampling")
plt.show()

# ---------- FEATURE ENGINEERING ----------

# Create hour only if the dataset contains Time
if "Time" in df.columns:
    df["hour"] = (df["Time"] // 3600) % 24
    print("Hour feature created.")
else:
    print("Time column not found. Skipping hour feature.")

# Create log_amount only if Amount exists
if "Amount" in df.columns:
    df["log_amount"] = np.log1p(df["Amount"].clip(lower=0))
    print("Log amount feature created.")
else:
    print("Amount column not found. Skipping log_amount feature.")

# ---------- FEATURES AND TARGET ----------
X = df.drop(columns=["Class"]).copy()
y = df["Class"].copy()

# Convert any non-numeric feature columns if necessary
X = X.apply(pd.to_numeric, errors="coerce")
X = X.replace([np.inf, -np.inf], np.nan)
X = X.fillna(X.median())

# ---------- TRAIN-TEST SPLIT ----------
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42,stratify=y)

# ---------- SCALING ----------
# Random Forest does not require scaling, but we keep RobustScaler
# for the original experiment and scale only available columns.
scale_cols = [
    col for col in ["Time", "Amount", "log_amount"]
    if col in X_train.columns
]

scaler = RobustScaler()
if scale_cols:
    X_train.loc[:, scale_cols] = scaler.fit_transform(X_train[scale_cols])
    X_test.loc[:, scale_cols] = scaler.transform(X_test[scale_cols])

# ---------- MODEL ----------
model = RandomForestClassifier(n_estimators=150,max_depth=12,class_weight="balanced_subsample",n_jobs=-1,random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
proba = model.predict_proba(X_test)[:, 1]

# ---------- METRICS ----------
print("\nModel Evaluation")
print("Accuracy :", round(accuracy_score(y_test, pred), 4))
print("Precision:", round(precision_score(y_test, pred, zero_division=0), 4))
print("Recall   :", round(recall_score(y_test, pred, zero_division=0), 4))
print("F1       :", round(f1_score(y_test, pred, zero_division=0), 4))
print("PR-AUC   :", round(average_precision_score(y_test, proba), 4))

# ---------- GRAPHS ----------
fig, ax = plt.subplots(1, 3, figsize=(19, 5))

sns.heatmap(
    confusion_matrix(y_test, pred),
    annot=True,
    fmt="d",
    cmap="Reds",
    ax=ax[0]
)
ax[0].set_title("Confusion Matrix")
ax[0].set_xlabel("Predicted")
ax[0].set_ylabel("Actual")

prec, rec, _ = precision_recall_curve(y_test, proba)
ax[1].plot(rec, prec)
ax[1].set_title("Precision-Recall Curve")
ax[1].set_xlabel("Recall")
ax[1].set_ylabel("Precision")

imp = pd.Series(
    model.feature_importances_,
    index=X.columns
).nlargest(10)

imp.sort_values().plot(kind="barh", ax=ax[2])
ax[2].set_title("Top 10 Feature Importances")

plt.tight_layout()
plt.show()

# ---------- EFFECT OF NUMBER OF TREES ----------
scores = []
tree_counts = [10, 25, 50, 100, 150]

for n in tree_counts:
    m = RandomForestClassifier(
        n_estimators=n,
        max_depth=12,
        class_weight="balanced_subsample",
        n_jobs=-1,
        random_state=42
    )

    m.fit(X_train, y_train)

    tree_proba = m.predict_proba(X_test)[:, 1]
    score = average_precision_score(y_test, tree_proba)
    scores.append(score)

    print(f"Trees: {n}, PR-AUC: {score:.4f}")

plt.plot(tree_counts, scores, marker="o")
plt.xlabel("Number of Trees")
plt.ylabel("PR-AUC")
plt.title("Effect of Number of Trees on Performance")
plt.show()
