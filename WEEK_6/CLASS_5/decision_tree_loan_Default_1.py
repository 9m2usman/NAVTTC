# ============================================================
# DECISION TREE - Loan default prediction + Loan recommendation
# German credit, OpenML API
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report)

# ---------- E: EXTRACT ----------
data = fetch_openml(name="credit-g", version=1, as_frame=True)
df = data.frame
print("Shape:", df.shape)
print(df.head())

# ---------- T: TRANSFORM ----------
df = df.drop_duplicates().dropna()
df["default"] = (df["class"] == "bad").astype(int)   # 1 = customer defaults
df = df.drop(columns=["class"])
sns.countplot(x="default", data=df)
plt.title("Loan default (1) vs repaid (0)")
plt.show()

# ---------- FEATURE ENGINEERING ----------
df["credit_per_month"] = df["credit_amount"] / df["duration"]
df["credit_per_age"] = df["credit_amount"] / df["age"]

# Convert text columns to numbers using one-hot encoding
X = pd.get_dummies(df.drop(columns=["default"]),drop_first=True)
y = df["default"]
print("Features after encoding:", X.shape[1])

# ---------- TRAIN / TEST SPLIT ----------
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

# Decision trees do not require feature scaling.
# ---------- FIND THE BEST TREE DEPTH ----------
depths = range(1, 16)
train_acc = []
test_acc = []
for d in depths:
    t = DecisionTreeClassifier(max_depth=d,random_state=42,class_weight="balanced")
    t.fit(X_train, y_train)
    train_acc.append(t.score(X_train, y_train))
    test_acc.append(t.score(X_test, y_test))

# ---------- OVERFITTING GRAPH ----------
plt.plot(depths,train_acc,label="Train accuracy")
plt.plot(depths,test_acc,label="Test accuracy")
plt.xlabel("max_depth")
plt.ylabel("Accuracy")
plt.title("Overfitting check: gap grows as the tree gets deeper")
plt.legend()
plt.show()
best_depth = depths[int(np.argmax(test_acc))]
print("Best depth:", best_depth)

# ---------- FINAL MODEL ----------
model = DecisionTreeClassifier(max_depth=best_depth,min_samples_leaf=10,class_weight="balanced",random_state=42)
model.fit(X_train,y_train)

# ---------- TEST PREDICTIONS ----------
pred = model.predict(X_test)

# ---------- METRICS ----------
print("Accuracy :",round(accuracy_score(y_test, pred), 4))
print("Precision:",round(precision_score(y_test, pred), 4))
print("Recall   :",round(recall_score(y_test, pred), 4))
print("F1       :",round(f1_score(y_test, pred), 4))
print(classification_report(y_test,pred))

# ---------- GRAPHS ----------
fig, ax = plt.subplots(1,2,figsize=(14, 5))

# Confusion matrix
sns.heatmap(confusion_matrix(y_test, pred),annot=True,fmt="d",cmap="Oranges",ax=ax[0])
ax[0].set_title("Confusion matrix")
ax[0].set_xlabel("Predicted")
ax[0].set_ylabel("Actual")

# Feature importance
imp = pd.Series(model.feature_importances_,index=X.columns).nlargest(10)
imp.sort_values().plot(kind="barh",ax=ax[1])
ax[1].set_title("Top 10 feature importances")
plt.tight_layout()
plt.show()

# ---------- DECISION TREE ----------
plt.figure(figsize=(22, 10))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Repaid","Default"],
    filled=True,
    max_depth=3,
    fontsize=8
)
plt.title("Decision tree (top 3 levels)")
plt.show()

# ============================================================
# NEW CUSTOMER LOAN DECISION
print("\n")
print("==============================================")
print("        NEW CUSTOMER LOAN DECISION")
print("==============================================")

# ---------- USER INPUT ----------
age = int(input("Enter customer age: "))
credit_amount = float(input("Enter requested loan amount: "))
duration = int(input("Enter loan duration in months: "))

# ---------- FEATURE ENGINEERING ----------
credit_per_month = (credit_amount / duration)
credit_per_age = (credit_amount / age)

# ---------- CREATE NEW CUSTOMER ----------
new_customer = pd.DataFrame({
    "age": [age],
    "credit_amount": [credit_amount],
    "duration": [duration],
    "credit_per_month": [credit_per_month],
    "credit_per_age": [credit_per_age]
})

# ============================================================
# ADD THE CATEGORICAL VALUES
checking_status = input("Enter checking status (low / medium / high): ").lower()
employment = input("Enter employment (unemployed / employed / highly_employed): ").lower()
new_customer["checking_status"] = checking_status
new_customer["employment"] = employment

# ---------- ONE-HOT ENCODING ----------
new_customer = pd.get_dummies(new_customer,drop_first=True)

# Make the new customer have exactly
# the same columns as the training data.
new_customer = new_customer.reindex(columns=X.columns,fill_value=0)

# ============================================================
# DECISION TREE PREDICTION
prediction = model.predict(new_customer)[0]

# ---------- PREDICTION PROBABILITY ----------
probability = model.predict_proba(new_customer)[0]
repaid_probability = probability[0]
default_probability = probability[1]
print("\n")
print("----------------------------------------------")
print("             MODEL PREDICTION")
print("----------------------------------------------")
if prediction == 0:
    print("Prediction: REPAID")
else:
    print("Prediction: DEFAULT")
print("Repaid probability:",round(repaid_probability * 100,2),"%")
print("Default probability:",round(default_probability * 100,2),"%")

# ============================================================
# CREDIT SCORE
# Convert model probability into
# a demonstration score from 300 to 850.
credit_score = (300 +(repaid_probability * 550))
credit_score = round(credit_score)
print("Credit score:",credit_score)

# ============================================================
# LOAN RECOMMENDATION
print("\n")
print("----------------------------------------------")
print("             LOAN RECOMMENDATION")
print("----------------------------------------------")
if credit_score >= 750:
    decision = "APPROVE"
    recommended_loan = credit_amount
    risk_level = "LOW"
elif credit_score >= 650:
    decision = "APPROVE WITH LIMIT"
    recommended_loan = (credit_amount * 0.70)
    risk_level = "MEDIUM"
elif credit_score >= 550:
    decision = "HIGH RISK - SMALL LOAN"
    recommended_loan = (credit_amount * 0.30)
    risk_level = "HIGH"
else:
    decision = "REJECT"
    recommended_loan = 0
    risk_level = "VERY HIGH"

# ============================================================
# FINAL RESULT
print("\n")
print("==============================================")
print("              FINAL LOAN DECISION")
print("==============================================")
print("Risk level:",risk_level)
print("Credit score:",credit_score)
print("Requested loan:",round(credit_amount,2))
print("Recommended loan:",round(recommended_loan,2))
print("Decision:",decision)
print("==============================================")