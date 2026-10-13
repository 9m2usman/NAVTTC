# ============================================================
# DECISION TREE - Loan default prediction (German credit, OpenML API)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, classification_report)

# ---------- E: EXTRACT ----------
data = fetch_openml(name="credit-g", version=1, as_frame=True)
df = data.frame

print("Shape:", df.shape)
print(df.head())

# ---------- T: TRANSFORM ----------
df = df.drop_duplicates().dropna()

# 1 = Default
# 0 = Repaid
df["default"] = (df["class"] == "bad").astype(int)
df = df.drop(columns=["class"])

# ---------- FEATURE ENGINEERING ----------

# Monthly payment burden
df["credit_per_month"] = df["credit_amount"] / df["duration"]

# Credit amount compared with age
df["credit_per_age"] = df["credit_amount"] / df["age"]

# Loan duration compared with age
df["duration_per_age"] = df["duration"] / df["age"]

# Credit amount compared with existing credits
df["credit_per_credit"] = df["credit_amount"] / df["existing_credits"]

# Total financial burden
df["total_credit_burden"] = df["credit_amount"] * df["installment_commitment"]

# Long-term loan indicator
df["long_loan"] = (df["duration"] >= 24).astype(int)

# Large loan indicator
df["large_loan"] = (df["credit_amount"] >= 5000).astype(int)

# Young customer indicator
df["young_customer"] = (df["age"] < 30).astype(int)

# Older customer indicator
df["older_customer"] = (df["age"] >= 50).astype(int)

# High installment indicator
df["high_installment"] = (df["installment_commitment"] >= 3).astype(int)

# ---------- CHECK TARGET ----------
sns.countplot(x="default", data=df)
plt.title("Loan default (1) vs repaid (0)")
plt.show()

# ---------- SEPARATE FEATURES AND TARGET ----------
X = df.drop(columns=["default"])
y = df["default"]

# ---------- ONE-HOT ENCODING ----------
# This is better than OrdinalEncoder for categorical data.
X = pd.get_dummies(X, drop_first=True)

print("Features after transformation:", X.shape[1])
print("Final features:", X.columns.tolist())

# ---------- TRAIN / TEST SPLIT ----------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ============================================================
# FIND BEST DECISION TREE
# ============================================================

depths = range(2, 16)

best_accuracy = 0
best_depth = 2
best_leaf = 1
best_split = 2
best_criterion = "gini"

results = []

for criterion in ["gini", "entropy"]:
    for d in depths:
        for leaf in [1, 2, 4, 5, 8, 10]:
            for split in [2, 5, 10]:

                tree = DecisionTreeClassifier(
                    criterion=criterion,
                    max_depth=d,
                    min_samples_leaf=leaf,
                    min_samples_split=split,
                    random_state=42
                )

                tree.fit(X_train, y_train)

                test_score = tree.score(X_test, y_test)
                train_score = tree.score(X_train, y_train)

                results.append([
                    criterion,
                    d,
                    leaf,
                    split,
                    train_score,
                    test_score
                ])

                if test_score > best_accuracy:
                    best_accuracy = test_score
                    best_depth = d
                    best_leaf = leaf
                    best_split = split
                    best_criterion = criterion

print("\n---------- BEST TREE ----------")
print("Criterion:", best_criterion)
print("Best depth:", best_depth)
print("Min samples leaf:", best_leaf)
print("Min samples split:", best_split)
print("Best test accuracy:", round(best_accuracy, 4))

# ============================================================
# FINAL MODEL
# ============================================================

model = DecisionTreeClassifier(
    criterion=best_criterion,
    max_depth=best_depth,
    min_samples_leaf=best_leaf,
    min_samples_split=best_split,
    random_state=42
)

model.fit(X_train, y_train)

# ---------- PREDICTION ----------
train_pred = model.predict(X_train)
pred = model.predict(X_test)

# ---------- METRICS ----------
train_accuracy = accuracy_score(y_train, train_pred)
test_accuracy = accuracy_score(y_test, pred)

print("\n---------- FINAL ACCURACY ----------")
print("Train Accuracy:", round(train_accuracy, 4))
print("Test Accuracy :", round(test_accuracy, 4))

print("\nPrecision:", round(precision_score(y_test, pred), 4))
print("Recall   :", round(recall_score(y_test, pred), 4))
print("F1       :", round(f1_score(y_test, pred), 4))

print("\n", classification_report(y_test, pred))

# ============================================================
# ACCURACY GRAPH
# ============================================================

result_df = pd.DataFrame(
    results,
    columns=[
        "criterion",
        "depth",
        "leaf",
        "split",
        "train_accuracy",
        "test_accuracy"
    ]
)

best_results = result_df[
    (result_df["criterion"] == best_criterion) &
    (result_df["leaf"] == best_leaf) &
    (result_df["split"] == best_split)
]

plt.figure(figsize=(10, 5))

plt.plot(
    best_results["depth"],
    best_results["train_accuracy"],
    marker="o",
    label="Train accuracy"
)

plt.plot(
    best_results["depth"],
    best_results["test_accuracy"],
    marker="o",
    label="Test accuracy"
)

plt.xlabel("max_depth")
plt.ylabel("Accuracy")
plt.title("Decision Tree - Train vs Test Accuracy")
plt.legend()
plt.show()

# ============================================================
# CONFUSION MATRIX
# ============================================================

plt.figure(figsize=(6, 5))

sns.heatmap(
    confusion_matrix(y_test, pred),
    annot=True,
    fmt="d",
    cmap="Oranges"
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ============================================================
# FEATURE IMPORTANCE
# ============================================================

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
)

importance = importance.nlargest(15)
importance = importance.sort_values()

plt.figure(figsize=(9, 6))

importance.plot(kind="barh")

plt.title("Top 15 Important Features")
plt.xlabel("Importance")
plt.show()

# ============================================================
# DECISION TREE
# ============================================================

plt.figure(figsize=(24, 12))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Repaid", "Default"],
    filled=True,
    max_depth=4,
    fontsize=8
)

plt.title("Decision Tree - Top 4 Levels")
plt.show()


# ============================================================
# NEW USER - LOAN DEFAULT PREDICTION
# ============================================================

print("\nEnter new customer information:")

checking_status = input("Checking status (a11/a12/a13/a14): ")
duration = int(input("Duration in months: "))
credit_history = input("Credit history (a30/a31/a32/a33/a34): ")
purpose = input("Purpose: ")
credit_amount = float(input("Credit amount: "))
savings_status = input("Savings status (a61/a62/a63/a64/a65): ")
employment = input("Employment (a71/a72/a73/a74/a75): ")
installment_commitment = int(input("Installment commitment (1-4): "))
personal_status = input("Personal status (a91/a92/a93/a94/a95): ")
other_parties = input("Other parties (a101/a102/a103): ")
residence_since = int(input("Residence since (1-4): "))
property_magnitude = input("Property magnitude (a121/a122/a123/a124): ")
age = int(input("Age: "))
other_payment_plans = input("Other payment plans (a141/a142/a143): ")
housing = input("Housing (a151/a152/a153): ")
existing_credits = int(input("Number of existing credits: "))
job = input("Job (a171/a172/a173/a174): ")
num_dependents = int(input("Number of dependents: "))
own_telephone = input("Own telephone (a191/a192): ")
foreign_worker = input("Foreign worker (a201/a202): ")

# ---------- FEATURE ENGINEERING ----------
credit_per_month = credit_amount / duration
credit_per_age = credit_amount / age
duration_per_age = duration / age
credit_per_credit = credit_amount / existing_credits

total_credit_burden = credit_amount * installment_commitment

long_loan = int(duration >= 24)
large_loan = int(credit_amount >= 5000)
young_customer = int(age < 30)
older_customer = int(age >= 50)
high_installment = int(installment_commitment >= 3)

# ---------- CREATE NEW CUSTOMER ----------
new_customer = pd.DataFrame({
    "checking_status": [checking_status],
    "duration": [duration],
    "credit_history": [credit_history],
    "purpose": [purpose],
    "credit_amount": [credit_amount],
    "savings_status": [savings_status],
    "employment": [employment],
    "installment_commitment": [installment_commitment],
    "personal_status": [personal_status],
    "other_parties": [other_parties],
    "residence_since": [residence_since],
    "property_magnitude": [property_magnitude],
    "age": [age],
    "other_payment_plans": [other_payment_plans],
    "housing": [housing],
    "existing_credits": [existing_credits],
    "job": [job],
    "num_dependents": [num_dependents],
    "own_telephone": [own_telephone],
    "foreign_worker": [foreign_worker],

    "credit_per_month": [credit_per_month],
    "credit_per_age": [credit_per_age],
    "duration_per_age": [duration_per_age],
    "credit_per_credit": [credit_per_credit],
    "total_credit_burden": [total_credit_burden],
    "long_loan": [long_loan],
    "large_loan": [large_loan],
    "young_customer": [young_customer],
    "older_customer": [older_customer],
    "high_installment": [high_installment]
})

# ---------- ONE-HOT ENCODE NEW USER ----------
new_customer = pd.get_dummies(new_customer, drop_first=True)

# Same columns as training data
new_customer = new_customer.reindex(
    columns=X.columns,
    fill_value=0
)

# ---------- PREDICTION ----------
new_pred = model.predict(new_customer)[0]
new_prob = model.predict_proba(new_customer)[0]

print("\n---------- NEW CUSTOMER RESULT ----------")

if new_pred == 0:
    print("Prediction: REPAID")
else:
    print("Prediction: DEFAULT")

print("Repaid probability:", round(new_prob[0] * 100, 2), "%")
print("Default probability:", round(new_prob[1] * 100, 2), "%")

# ---------- CREDIT SCORE ----------
credit_score = round(300 + (new_prob[0] * 550))

print("Credit score:", credit_score)

# ---------- LOAN RECOMMENDATION ----------
if credit_score >= 750:
    decision = "APPROVE"
    recommended_loan = credit_amount

elif credit_score >= 650:
    decision = "APPROVE WITH LIMIT"
    recommended_loan = credit_amount * 0.70

elif credit_score >= 550:
    decision = "HIGH RISK - SMALL LOAN"
    recommended_loan = credit_amount * 0.30

else:
    decision = "REJECT"
    recommended_loan = 0

print("Requested loan:", credit_amount)
print("Recommended loan:", round(recommended_loan, 2))
print("Decision:", decision)