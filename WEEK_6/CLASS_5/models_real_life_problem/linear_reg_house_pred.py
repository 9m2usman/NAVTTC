# ============================================================
# LINEAR REGRESSION - House price prediction (Boston housing)
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ---------- E: EXTRACT (read directly from a URL) ----------
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(url)
print("Shape:", df.shape)
print(df.head())

# ---------- T: TRANSFORM (cleaning) ----------
df = df.drop(columns=["b"])          # drop ethically problematic column
df = df.drop_duplicates().dropna()   # remove duplicate rows and missing values
print("\nMissing values:\n", df.isnull().sum().sum())

# Target = medv (median house value in $1000s)
# Linear regression is sensitive to outliers, so cap the target at the 99th percentile
df["medv"] = df["medv"].clip(upper=df["medv"].quantile(0.99))

# ---------- EDA graphs ----------
plt.figure(figsize=(10, 7))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation heatmap")
plt.show()

df["medv"].hist(bins=30)
plt.title("House price distribution")
plt.xlabel("medv")
plt.show()

# ---------- FEATURE ENGINEERING (adding new features) ----------
df["lstat_log"] = np.log1p(df["lstat"])      # lstat is skewed, log makes it more linear
df["rm_squared"] = df["rm"] ** 2             # rooms effect is curved, not straight
df["tax_per_room"] = df["tax"] / df["rm"]    # tax burden per room

# ---------- Helper to train and evaluate with a given feature list ----------
def run_model(features, label):
    X = df[features]
    y = df["medv"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # SCALING: fit on train only, then apply to test (avoids data leakage)
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_s, y_train)
    pred = model.predict(X_test_s)

    print(f"\n--- {label} ---")
    print("MAE :", round(mean_absolute_error(y_test, pred), 3))
    print("RMSE:", round(np.sqrt(mean_squared_error(y_test, pred)), 3))
    print("R2  :", round(r2_score(y_test, pred), 3))
    return model, y_test, pred, features

base_features = ["crim", "zn", "indus", "chas", "nox", "rm", "age","dis", "rad", "tax", "ptratio", "lstat"]
new_features = base_features + ["lstat_log", "rm_squared", "tax_per_room"]

run_model(base_features, "Baseline features")
model, y_test, pred, feats = run_model(new_features, "With new features")

# ---------- GRAPHS for the final model ----------
fig, ax = plt.subplots(1, 3, figsize=(18, 5))

# 1) Actual vs predicted (points near the red line = good model)
ax[0].scatter(y_test, pred, alpha=0.6)
ax[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
ax[0].set_title("Actual vs Predicted")
ax[0].set_xlabel("Actual"); ax[0].set_ylabel("Predicted")

# 2) Residuals (should be randomly scattered around 0)
residuals = y_test - pred
ax[1].scatter(pred, residuals, alpha=0.6)
ax[1].axhline(0, color="r", linestyle="--")
ax[1].set_title("Residual plot")
ax[1].set_xlabel("Predicted"); ax[1].set_ylabel("Residual")

# 3) Coefficients = importance of each (scaled) feature
coef = pd.Series(model.coef_, index=feats).sort_values()
coef.plot(kind="barh", ax=ax[2])
ax[2].set_title("Feature coefficients")
plt.tight_layout()
plt.show()