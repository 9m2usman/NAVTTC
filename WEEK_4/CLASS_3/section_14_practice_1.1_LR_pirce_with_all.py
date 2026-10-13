import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("./Datasets/housing.csv")
print(df)

# Convert Area from square feet to Marla
df["Area"] = df["Area"] / 272.25

print(df.columns.to_list())

# Convert text columns into numbers
df["Location"] = df["Location"].astype("category").cat.codes
df["Condition"] = df["Condition"].astype("category").cat.codes
df["Garage"] = df["Garage"].astype("category").cat.codes

# or another way use our own labelEncoding
# df["Location"] = LabelEncoder().fit_transform(df["Location"])
# df["Condition"] = LabelEncoder().fit_transform(df["Condition"])
# df["Garage"] = LabelEncoder().fit_transform(df["Garage"])

col_list = df.columns.to_list()
split = int(len(df) * 0.8)
df1 = df.iloc[split:]   # 20%
df2 = df.iloc[:split]   # 80%

df1.to_csv("housing_test.csv", index=False)
df2.to_csv("housing_train.csv", index=False)


# Training data
train = pd.read_csv("housing_train.csv")

# Features
features = df.columns.to_list()[1:-1]
# or fetures = df.columns.to_list()[1:len(df.columns)-1]

# Mean of train price
price_mean = sum(train["Price"]) / len(train)
print("mean price :", price_mean)

# Store slopes
slopes = []

# Calculate slope for every feature
for feature in features:
    # Mean of current feature
    feature_mean = sum(train[feature]) / len(train)
    # dev(x), dev(y), dev(x)*dev(y), [dev(x)]**2
    dev_x = []
    dev_y = []
    product_dev = []
    square_dev_x = []

    # Nested loop
    for i in range(len(train)):
        dx = train[feature][i] - feature_mean
        dy = train["Price"][i] - price_mean
        product = dx * dy
        square = dx ** 2
        dev_x.append(dx)
        dev_y.append(dy)
        product_dev.append(product)
        square_dev_x.append(square)

    # Same formula you used before
    slope = sum(product_dev) / sum(square_dev_x)
    slopes.append(slope)
    print(feature, "Slope m :", slope)

# Find intercept
intercept = price_mean
for i in range(len(features)):
    feature_mean = sum(train[features[i]]) / len(train)
    intercept = intercept - (slopes[i] * feature_mean)
print("a constant/intercept/weight :", intercept)

# Training prediction
for i in range(len(train)):
    prediction = intercept
    for j in range(len(features)):
        prediction = prediction + (slopes[j] * train[features[j]][i])

    train["predict_price"] =0.0
    train.loc[i, "predicted_rice"] = int(prediction)


# Training done now move to testing phase..
test = pd.read_csv("housing_test.csv")

# Predict first test house
prediction = intercept
for i in range(len(features)):
    prediction = prediction + (slopes[i] * test[features[i]][0])

print("Actual Price :", test["Price"][0])
print("Predicted Price :", int(prediction))

new_house = [12, 4, 3, 2, 2020, 1, 2, 1]
new_house_price = intercept
for i in range(len(new_house)):
    new_house_price = new_house_price + slopes[i] * new_house[i]

print("New house predicted price : ",new_house_price)


# # < ======================== Built-in linear regression ======================== > 
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("./Datasets/housing.csv")

print(df)

# Convert Area from square feet to Marla
df["Area"] = df["Area"] / 272.25

# Convert text columns into numbers
df["Location"] = df["Location"].astype("category").cat.codes
df["Condition"] = df["Condition"].astype("category").cat.codes
df["Garage"] = df["Garage"].astype("category").cat.codes

# Split data into 80% train and 20% test
split = int(len(df) * 0.8)

train = df.iloc[:split]
test = df.iloc[split:]

# Features
features = df.columns.to_list()[1:-1]

# Training data
X_train = train[features]
y_train = train["Price"]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Show slopes
print("Slopes :", model.coef_)

# Show intercept
print("Intercept :", model.intercept_)

# Predict prices for test data
predicted_price = model.predict(test[features])

# Make a copy of test data
test = test.copy()

# Add predicted prices to test data
test["Predicted_Price"] = predicted_price

# Show actual and predicted prices
print(test[features + ["Price", "Predicted_Price"]])

# -----------------------------
# Model Evaluation
# -----------------------------

actual = test["Price"]

# Mean Absolute Error
print("MAE :", mean_absolute_error(actual, predicted_price))

# R2 Score
print("R2 Score :", r2_score(actual, predicted_price))