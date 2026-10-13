# ============================================================
# GRADIENT BOOSTING - Credit scoring (Default of credit card clients, OpenML API)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,f1_score, confusion_matrix, roc_curve,roc_auc_score, log_loss)

# ---------- E: EXTRACT ----------
data = fetch_openml(data_id=42477, as_frame=True)
df = data.frame.copy()
print("Shape:", df.shape)

# Give columns readable names (same order as the original UCI dataset)
df.columns = (["limit_bal", "sex", "education", "marriage", "age"]
              + [f"pay_{i}" for i in range(1, 7)]       # repayment status per month
              + [f"bill_{i}" for i in range(1, 7)]      # bill amount per month
              + [f"paid_{i}" for i in range(1, 7)]      # amount paid per month
              + ["default"])

# ---------- T: TRANSFORM ----------
df = df.drop_duplicates().dropna()
df["default"] = df["default"].astype(int)    # 1 = customer defaulted
# Fix undocumented category codes
df["education"] = df["education"].astype(float).replace({0: 4, 5: 4, 6: 4})
df["marriage"] = df["marriage"].astype(float).replace({0: 3})
df = df.astype(float)

sns.countplot(x="default", data=df)
plt.title("Default (1) vs no default (0)")
plt.show()

# ---------- FEATURE ENGINEERING ----------
bill_cols = [f"bill_{i}" for i in range(1, 7)]
paid_cols = [f"paid_{i}" for i in range(1, 7)]
pay_cols = [f"pay_{i}" for i in range(1, 7)]

df["avg_bill"] = df[bill_cols].mean(axis=1)                       # average monthly bill
df["utilization"] = df["avg_bill"] / (df["limit_bal"] + 1)        # how much of the limit is used
df["pay_ratio"] = df[paid_cols].sum(axis=1) / (df[bill_cols].sum(axis=1).abs() + 1)
df["months_late"] = (df[pay_cols] > 0).sum(axis=1)                # count of late months

X = df.drop(columns=["default"])
y = df["default"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# NOTE: Boosted trees split on thresholds, so scaling is not needed (same as Decision Tree).
# ---------- Model ----------
model = GradientBoostingClassifier(
    n_estimators=200,      # number of small trees added one by one
    learning_rate=0.1,     # how much each tree contributes
    max_depth=3,           # keep trees shallow (weak learners)
    subsample=0.8,         # each tree sees 80% of rows, reduces overfitting
    random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
proba = model.predict_proba(X_test)[:, 1]

# ---------- Metrics ----------
print("Accuracy :", round(accuracy_score(y_test, pred), 4))
print("Precision:", round(precision_score(y_test, pred), 4))
print("Recall   :", round(recall_score(y_test, pred), 4))
print("F1       :", round(f1_score(y_test, pred), 4))
print("ROC-AUC  :", round(roc_auc_score(y_test, proba), 4))

# ---------- Graphs ----------
fig, ax = plt.subplots(2, 2, figsize=(15, 11))

# 1) Learning curve: loss after each added tree (shows when to stop)
train_loss = [log_loss(y_train, p) for p in model.staged_predict_proba(X_train)]
test_loss = [log_loss(y_test, p) for p in model.staged_predict_proba(X_test)]
ax[0, 0].plot(train_loss, label="Train loss")
ax[0, 0].plot(test_loss, label="Test loss")
ax[0, 0].set_title("Loss vs number of trees")
ax[0, 0].set_xlabel("Trees"); ax[0, 0].set_ylabel("Log loss")
ax[0, 0].legend()

# 2) Confusion matrix
sns.heatmap(confusion_matrix(y_test, pred), annot=True, fmt="d",cmap="Greens", ax=ax[0, 1])
ax[0, 1].set_title("Confusion matrix")

# 3) ROC curve
fpr, tpr, _ = roc_curve(y_test, proba)
ax[1, 0].plot(fpr, tpr, label=f"AUC = {roc_auc_score(y_test, proba):.3f}")
ax[1, 0].plot([0, 1], [0, 1], "r--")
ax[1, 0].set_title("ROC curve")
ax[1, 0].legend()

# 4) Feature importance
imp = pd.Series(model.feature_importances_, index=X.columns).nlargest(10)
imp.sort_values().plot(kind="barh", ax=ax[1, 1])
ax[1, 1].set_title("Top 10 features (look for our new ones)")
plt.tight_layout()
plt.show()