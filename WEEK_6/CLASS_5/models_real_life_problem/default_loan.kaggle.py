# ============================================================
# DECISION TREE - Loan approval prediction (simple version)
# ============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# ---------- 1. LOAD DATA ----------
df = pd.read_csv("loan_data_set.csv")
print("Shape:", df.shape)
print(df.head())
print("\nMissing values:\n", df.isnull().sum())

# ---------- 2. TRANSFORMATION (cleaning) ----------
df = df.drop(columns=["Loan_ID"])           # ID is not useful for prediction
df = df.drop_duplicates()

# Fill missing values
# text columns -> most common value (mode)
for col in ["Gender", "Married", "Dependents", "Self_Employed", "Credit_History"]:
    df[col] = df[col].fillna(df[col].mode()[0])

# number columns -> median (middle value, not affected by outliers)
for col in ["LoanAmount", "Loan_Amount_Term"]:
    df[col] = df[col].fillna(df[col].median())

# Convert text to numbers
df["Dependents"] = df["Dependents"].replace("3+", "3").astype(int)
df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})
df["Married"] = df["Married"].map({"Yes": 1, "No": 0})
df["Education"] = df["Education"].map({"Graduate": 1, "Not Graduate": 0})
df["Self_Employed"] = df["Self_Employed"].map({"Yes": 1, "No": 0})
df["Property_Area"] = df["Property_Area"].map({"Rural": 0, "Semiurban": 1, "Urban": 2})
df["Loan_Status"] = df["Loan_Status"].map({"Y": 1, "N": 0})   # 1 = approved

# ---------- 3. FEATURE ENGINEERING (new columns) ----------
df["TotalIncome"] = df["ApplicantIncome"] + df["CoapplicantIncome"]
df["EMI"] = df["LoanAmount"] * 1000 / df["Loan_Amount_Term"]        # monthly installment
df["IncomeAfterEMI"] = df["TotalIncome"] - df["EMI"]                # money left after paying EMI
df["LoanToIncome"] = df["LoanAmount"] * 1000 / df["TotalIncome"]    # loan size vs income

print("\nMissing values after cleaning:", df.isnull().sum().sum())

# ---------- 4. GRAPHS BEFORE MODEL ----------
sns.countplot(x="Loan_Status", data=df)
plt.title("Approved (1) vs Rejected (0)")
plt.show()

sns.countplot(x="Credit_History", hue="Loan_Status", data=df)
plt.title("Credit history vs loan status")
plt.show()

# ---------- 5. SPLIT DATA ----------
X = df.drop(columns=["Loan_Status"])
y = df["Loan_Status"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
# (Decision trees do not need scaling)

# ---------- 6. FIND BEST DEPTH (overfitting / underfitting) ----------
# depth too small  -> underfitting (model too simple)
# depth too large  -> overfitting (model memorizes the training data)
train_scores = []
cv_scores = []
depths = range(2, 11)

for d in depths:
    tree = DecisionTreeClassifier(max_depth=d, min_samples_leaf=5, random_state=42)
    tree.fit(X_train, y_train)
    train_scores.append(tree.score(X_train, y_train))
    # cross validation = test on parts of the TRAIN data (test data stays untouched)
    cv_scores.append(cross_val_score(tree, X_train, y_train, cv=5).mean())

best_depth = list(depths)[np.argmax(cv_scores)]
print("\nBest depth:", best_depth)

plt.plot(depths, train_scores, marker="o", label="Train accuracy")
plt.plot(depths, cv_scores, marker="o", label="Validation accuracy")
plt.xlabel("max_depth")
plt.ylabel("Accuracy")
plt.title("Depth vs accuracy (gap = overfitting)")
plt.legend()
plt.show()

# ---------- 7. TRAIN FINAL MODEL ----------
# max_depth and min_samples_leaf keep the tree small, so it cannot overfit
model = DecisionTreeClassifier(max_depth=best_depth, min_samples_leaf=5, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)

# ---------- 8. OVERFITTING CHECK ----------
# Compare with a tree that has no limits
big_tree = DecisionTreeClassifier(random_state=42)
big_tree.fit(X_train, y_train)

print("\n--- Overfitting check ---")
print("Unlimited tree -> Train:", round(big_tree.score(X_train, y_train), 3),
      "| Test:", round(big_tree.score(X_test, y_test), 3))
print("Final tree     -> Train:", round(model.score(X_train, y_train), 3),
      "| Test:", round(model.score(X_test, y_test), 3))
print("Always predict Approved:", round(y_train.mean(), 3), "(our model must beat this)")

# ---------- 9. METRICS ----------
print("\nAccuracy :", round(accuracy_score(y_test, pred), 4))
print("Precision:", round(precision_score(y_test, pred), 4))
print("Recall   :", round(recall_score(y_test, pred), 4))
print("F1 score :", round(f1_score(y_test, pred), 4))
print(classification_report(y_test, pred, target_names=["Rejected", "Approved"]))

# ---------- 10. GRAPHS AFTER MODEL ----------
# Confusion matrix
sns.heatmap(confusion_matrix(y_test, pred), annot=True, fmt="d", cmap="Blues")
plt.title("Confusion matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Feature importance
importance = pd.Series(model.feature_importances_, index=X.columns)
importance.sort_values().plot(kind="barh")
plt.title("Feature importance")
plt.show()

# The tree itself
plt.figure(figsize=(18, 8))
plot_tree(model, feature_names=X.columns, class_names=["Rejected", "Approved"],
          filled=True, fontsize=8)
plt.title("Decision tree")
plt.show()

# ============================================================
# 11. NEW APPLICANT PREDICTION
# ============================================================
print("\nEnter new applicant information:")
gender = input("Gender (Male/Female): ")
married = input("Married (Yes/No): ")
dependents = input("Dependents (0/1/2/3): ")
education = input("Education (Graduate/Not Graduate): ")
self_employed = input("Self employed (Yes/No): ")
applicant_income = float(input("Applicant monthly income: "))
coapplicant_income = float(input("Coapplicant monthly income (0 if none): "))
loan_amount = float(input("Loan amount in THOUSANDS (150 = 150,000): "))
loan_term = float(input("Loan term in months (e.g. 360): "))
credit_history = float(input("Credit history (2=new, 1 = good, 0 = bad): "))
property_area = input("Property area (Rural/Semiurban/Urban): ")

# Same transformation and features as the training data
total_income = applicant_income + coapplicant_income
emi = loan_amount * 1000 / loan_term

new_customer = pd.DataFrame({
    "Gender": [1 if gender == "Male" or gender == "M" or gender == "m" else 0],
    "Married": [1 if married == "Yes" or married == "Y" or married == "y" else 0],
    "Dependents": [int(dependents.replace("+", ""))],
    "Education": [1 if education == "Graduate" or education == "G" or education == "g" else 0],
    "Self_Employed": [1 if self_employed == "Yes" or self_employed == "Y" or self_employed == "y" else 0],
    "ApplicantIncome": [applicant_income],
    "CoapplicantIncome": [coapplicant_income],
    "LoanAmount": [loan_amount],
    "Loan_Amount_Term": [loan_term],
    "Credit_History": [credit_history],
    "Property_Area": [{"Rural": 0, "Semiurban": 1, "Urban": 2}[property_area]],
    "TotalIncome": [total_income],
    "EMI": [emi],
    "IncomeAfterEMI": [total_income - emi],
    "LoanToIncome": [loan_amount * 1000 / total_income],
})

# Same column order as training data
new_customer = new_customer[X.columns]
new_pred = model.predict(new_customer)[0]
new_prob = model.predict_proba(new_customer)[0]   # [rejected, approved]
print("\n---------- RESULT ----------")
print("Prediction:", "APPROVED" if new_pred == 1 else "REJECTED")
print("Approval probability :", round(new_prob[1] * 100, 2), "%")
print("Rejection probability:", round(new_prob[0] * 100, 2), "%")

# Credit score and loan recommendation
credit_score = round(300 + new_prob[1] * 550)
requested = loan_amount * 1000
print("Credit score:", credit_score)
if credit_score >= 750:
    decision, recommended = "APPROVE", requested
elif credit_score >= 650:
    decision, recommended = "APPROVE WITH LIMIT", requested * 0.70
elif credit_score >= 550:
    decision, recommended = "HIGH RISK - SMALL LOAN", requested * 0.30
else:
    decision, recommended = "REJECT", 0
print("Requested loan  :", requested)
print("Recommended loan:", round(recommended, 2))
print("Decision        :", decision)