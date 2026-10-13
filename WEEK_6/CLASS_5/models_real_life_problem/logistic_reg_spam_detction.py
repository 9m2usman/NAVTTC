# ============================================================
# LOGISTIC REGRESSION - Spam detection (Spambase from OpenML API)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score,f1_score, confusion_matrix, roc_curve, roc_auc_score)

# ---------- E: EXTRACT from the OpenML API ----------
data = fetch_openml(data_id=44, as_frame=True)   # Spambase
df = data.frame
print("Shape:", df.shape)

# ---------- T: TRANSFORM ----------
df = df.drop_duplicates().dropna()
df["class"] = df["class"].astype(int)            # 1 = spam, 0 = not spam
print(df["class"].value_counts())

sns.countplot(x="class", data=df)
plt.title("Spam (1) vs Not spam (0)")
plt.show()

# ---------- FEATURE ENGINEERING ----------
word_cols = [c for c in df.columns if c.startswith("word_freq")]
char_cols = [c for c in df.columns if c.startswith("char_freq")]
cap_cols = [c for c in df.columns if c.startswith("capital_run")]

df["total_word_freq"] = df[word_cols].sum(axis=1)   # overall "wordiness"
df["total_char_freq"] = df[char_cols].sum(axis=1)   # lots of !, $ etc. = spammy

# Capital-letter columns are heavily skewed, so use log to squash big values
for c in cap_cols:
    df[c] = np.log1p(df[c])

# ---------- Split ----------
X = df.drop(columns=["class"])
y = df["class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ---------- SCALING (logistic regression needs it to converge well) ----------
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# ---------- Model ----------
model = LogisticRegression(max_iter=2000)
model.fit(X_train_s, y_train)
pred = model.predict(X_test_s)
proba = model.predict_proba(X_test_s)[:, 1]   # probability of being spam

# ---------- Metrics ----------
print("Accuracy :", round(accuracy_score(y_test, pred), 4))
print("Precision:", round(precision_score(y_test, pred), 4))
print("Recall   :", round(recall_score(y_test, pred), 4))
print("F1       :", round(f1_score(y_test, pred), 4))
print("ROC-AUC  :", round(roc_auc_score(y_test, proba), 4))

# ---------- Graphs ----------
fig, ax = plt.subplots(1, 3, figsize=(19, 5))

# 1) Confusion matrix
sns.heatmap(confusion_matrix(y_test, pred), annot=True, fmt="d",cmap="Blues", ax=ax[0])
ax[0].set_title("Confusion matrix")
ax[0].set_xlabel("Predicted"); ax[0].set_ylabel("Actual")

# 2) ROC curve
fpr, tpr, _ = roc_curve(y_test, proba)
ax[1].plot(fpr, tpr, label=f"AUC = {roc_auc_score(y_test, proba):.3f}")
ax[1].plot([0, 1], [0, 1], "r--")
ax[1].set_title("ROC curve")
ax[1].set_xlabel("False positive rate"); ax[1].set_ylabel("True positive rate")
ax[1].legend()

# 3) Top coefficients (positive = pushes toward spam)
coef = pd.Series(model.coef_[0], index=X.columns).sort_values()
pd.concat([coef.head(8), coef.tail(8)]).plot(kind="barh", ax=ax[2])
ax[2].set_title("Top words/features for ham (left) and spam (right)")
plt.tight_layout()
plt.show()