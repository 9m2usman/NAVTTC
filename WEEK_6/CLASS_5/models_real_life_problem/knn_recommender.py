# ============================================================
# KNN - Wine quality classification + "similar wine" recommender
# Data from the UCI repository, read directly with pandas
# ============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors
from sklearn.metrics import (accuracy_score, precision_score, recall_score,f1_score, confusion_matrix)

# ---------- E: EXTRACT ----------
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=";")
print("Shape:", df.shape)

# ---------- T: TRANSFORM ----------
df = df.drop_duplicates().dropna().reset_index(drop=True)
df["good"] = (df["quality"] >= 6).astype(int)    # 1 = good wine, 0 = average

sns.countplot(x="good", data=df)
plt.title("Good (1) vs average (0) wines")
plt.show()

# ---------- FEATURE ENGINEERING ----------
df["total_acidity"] = df["fixed acidity"] + df["volatile acidity"] + df["citric acid"]
df["free_sulfur_ratio"] = df["free sulfur dioxide"] / df["total sulfur dioxide"]
df["alcohol_sulphates"] = df["alcohol"] * df["sulphates"]

X = df.drop(columns=["quality", "good"])
y = df["good"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ---------- SCALING (very important for KNN, it uses distance) ----------
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# ---------- Choose the best K using cross validation ----------
k_values = range(1, 31)
cv_scores = []
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    cv_scores.append(cross_val_score(knn, X_train_s, y_train, cv=5).mean())

best_k = k_values[int(np.argmax(cv_scores))]
plt.plot(k_values, cv_scores, marker="o")
plt.axvline(best_k, color="r", linestyle="--", label=f"Best K = {best_k}")
plt.xlabel("K"); plt.ylabel("CV accuracy")
plt.title("Choosing K (small K overfits, large K underfits)")
plt.legend()
plt.show()

# ---------- Final model ----------
model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(X_train_s, y_train)
pred = model.predict(X_test_s)

# ---------- Metrics ----------
print("Accuracy :", round(accuracy_score(y_test, pred), 4))
print("Precision:", round(precision_score(y_test, pred), 4))
print("Recall   :", round(recall_score(y_test, pred), 4))
print("F1       :", round(f1_score(y_test, pred), 4))

sns.heatmap(confusion_matrix(y_test, pred), annot=True, fmt="d", cmap="Purples")
plt.title("Confusion matrix")
plt.xlabel("Predicted"); plt.ylabel("Actual")
plt.show()

# ---------- RECOMMENDER PART ----------
# "Customers who liked this wine will like these similar wines"
X_all_s = scaler.transform(X)                       # scale the full catalogue
nn = NearestNeighbors(n_neighbors=6).fit(X_all_s)   # 6 = itself + 5 recommendations

wine_id = 10                                        # change this to try other wines
distances, indices = nn.kneighbors(X_all_s[[wine_id]])
recs = indices[0][1:]                               # skip the first (the wine itself)

print(f"\nWine #{wine_id}:")
print(df.loc[wine_id, ["alcohol", "volatile acidity", "sulphates", "quality"]])
print("\nRecommended similar wines:")
print(df.loc[recs, ["alcohol", "volatile acidity", "sulphates", "quality"]])

# Visualise the neighbours on two features
plt.figure(figsize=(7, 5))
plt.scatter(df["alcohol"], df["volatile acidity"], alpha=0.2, label="All wines")
plt.scatter(df.loc[recs, "alcohol"], df.loc[recs, "volatile acidity"],color="green", s=80, label="Recommended")
plt.scatter(df.loc[wine_id, "alcohol"], df.loc[wine_id, "volatile acidity"],color="red", s=120, marker="*", label="Chosen wine")
plt.xlabel("Alcohol"); plt.ylabel("Volatile acidity")
plt.title("KNN recommendations")
plt.legend()
plt.show()