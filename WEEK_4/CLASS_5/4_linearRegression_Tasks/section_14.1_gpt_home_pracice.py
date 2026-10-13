import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("./Datasets/pakistan_dataset.csv")

# shape, col, null_values, datatypes
print(df.shape,df.columns,df.dtypes)

# sort by ID
df = df.sort_values("ID").reset_index(drop=True)

# duplicate rows
print("\nDuplicated Rows :",df.duplicated().sum())
df = df.drop_duplicates()
print("Shape after duplicates :",df.shape)

# null values
print("\nNull Values :")
print(df.isnull().sum())

# convert Area_SqFt, Year_Built and Price_PKR
df["Area_SqFt"] = df["Area_SqFt"].astype(str).str.replace(",","").str.extract(r"(\d+(?:\.\d+)?)")[0].astype(float)
df["Year_Built"] = df["Year_Built"].astype(str).str.extract(r"(\d{4})")[0].astype(float)
df["Price_PKR"] = df["Price_PKR"].astype(str).str.replace(",","").str.extract(r"(\d+(?:\.\d+)?)")[0].astype(float)

# clean string values before one hot encoding
string_columns = df.select_dtypes(include="str").columns

for col in string_columns:
    df[col] = df[col].astype(str).str.strip().str.lower()

# convert empty strings into null
for col in string_columns:
    df[col] = df[col].replace("",np.nan)

# check empty values
print("\nEmpty String Values :")
print(df[string_columns].isnull().sum())

# target missing values
# Price is the target, so rows without real prices cannot be used
print("\nMissing Prices :",df["Price_PKR"].isnull().sum())
df = df.dropna(subset=["Price_PKR"]).copy()
print("Shape after removing missing prices :",df.shape)

# numeric and string columns
integer_columns_df = df.select_dtypes(include="int").columns
float_columns_df = df.select_dtypes(include="float").columns
string_columns_df = df.select_dtypes(include="str").columns

print("\nInteger Columns :")
print(integer_columns_df)

print("\nFloat Columns :")
print(float_columns_df)

print("\nString Columns :")
print(string_columns_df)

# fill numeric null values with median
for col in float_columns_df:
    if col != "Price_PKR":
        df[col] = df[col].fillna(df[col].median())

# fill string null values
for col in string_columns_df:
    df[col] = df[col].fillna("unknown")

# remove impossible area values
print("\nArea values <= 0 :",sum(df["Area_SqFt"] <= 0))
df = df[df["Area_SqFt"] > 0].copy()

# remove extremely small property areas
print("Area values < 200 :",sum(df["Area_SqFt"] < 200))
df = df[df["Area_SqFt"] >= 200].copy()

# remove impossible year values
print("\nYear values < 1900 :",sum(df["Year_Built"] < 1900))
print("Year values > 2026 :",sum(df["Year_Built"] > 2026))

df.loc[(df["Year_Built"] < 1900) | (df["Year_Built"] > 2026),"Year_Built"] = np.nan
df["Year_Built"] = df["Year_Built"].fillna(df["Year_Built"].median())

# remove impossible price values
print("\nPrices <= 0 :",sum(df["Price_PKR"] <= 0))
df = df[df["Price_PKR"] > 0].copy()

# remove extreme price values
print("\nPrices >= 1 Billion :",sum(df["Price_PKR"] >= 1000000000))
df = df[df["Price_PKR"] < 1000000000].copy()

# price information
print("\nPrice Information")
print("Minimum Price :",df["Price_PKR"].min())
print("Maximum Price :",df["Price_PKR"].max())
print("Mean Price :",df["Price_PKR"].mean())
print("Median Price :",df["Price_PKR"].median())

# highest prices
print("\nHighest Prices")
print(df[["ID","Area_SqFt","City","Location","Property_Type","Price_PKR"]].sort_values("Price_PKR",ascending=False).head(10))

# lowest prices
print("\nLowest Prices")
print(df[["ID","Area_SqFt","City","Location","Property_Type","Price_PKR"]].sort_values("Price_PKR").head(10))

# price per square feet
# this is only for checking relationship and suspicious values
df["Price_per_SqFt"] = df["Price_PKR"] / df["Area_SqFt"]

print("\nPrice per SqFt Information")
print("Minimum :",df["Price_per_SqFt"].min())
print("Maximum :",df["Price_per_SqFt"].max())
print("Mean :",df["Price_per_SqFt"].mean())
print("Median :",df["Price_per_SqFt"].median())

# suspicious price per square feet
print("\nLowest Price per SqFt")
print(df[["ID","Area_SqFt","City","Location","Property_Type","Price_PKR","Price_per_SqFt"]].sort_values("Price_per_SqFt").head(10))

print("\nHighest Price per SqFt")
print(df[["ID","Area_SqFt","City","Location","Property_Type","Price_PKR","Price_per_SqFt"]].sort_values("Price_per_SqFt",ascending=False).head(10))

# suspicious area values
print("\nVery Small Areas")
print(df[["ID","Area_SqFt","City","Location","Property_Type","Price_PKR","Price_per_SqFt"]].sort_values("Area_SqFt").head(10))

print("\nVery Large Areas")
print(df[["ID","Area_SqFt","City","Location","Property_Type","Price_PKR","Price_per_SqFt"]].sort_values("Area_SqFt",ascending=False).head(10))

# remove clearly suspicious very large areas
print("\nArea values >= 15000 :",sum(df["Area_SqFt"] >= 15000))
df = df[df["Area_SqFt"] < 15000].copy()

# remove price per square feet diagnostic column
# it contains Price_PKR, so it would cause target leakage
df = df.drop(columns=["Price_per_SqFt"])

# add property age
df["Property_Age"] = 2026 - df["Year_Built"]

print("\nProperty Age Information")
print("Minimum :",df["Property_Age"].min())
print("Maximum :",df["Property_Age"].max())
print("Mean :",df["Property_Age"].mean())
print("Median :",df["Property_Age"].median())

# area per bedroom
df["Area_per_Bedroom"] = df["Area_SqFt"] / df["Bedrooms"].replace(0,np.nan)
df["Area_per_Bedroom"] = df["Area_per_Bedroom"].replace([np.inf,-np.inf],np.nan)
df["Area_per_Bedroom"] = df["Area_per_Bedroom"].fillna(df["Area_per_Bedroom"].median())

# area per bathroom
df["Area_per_Bathroom"] = df["Area_SqFt"] / df["Bathrooms"].replace(0,np.nan)
df["Area_per_Bathroom"] = df["Area_per_Bathroom"].replace([np.inf,-np.inf],np.nan)
df["Area_per_Bathroom"] = df["Area_per_Bathroom"].fillna(df["Area_per_Bathroom"].median())

# bedrooms per bathroom
df["Bedrooms_per_Bathroom"] = df["Bedrooms"] / df["Bathrooms"].replace(0,np.nan)
df["Bedrooms_per_Bathroom"] = df["Bedrooms_per_Bathroom"].replace([np.inf,-np.inf],np.nan)
df["Bedrooms_per_Bathroom"] = df["Bedrooms_per_Bathroom"].fillna(df["Bedrooms_per_Bathroom"].median())

# log area
df["Log_Area"] = np.log1p(df["Area_SqFt"])

# area squared
df["Area_Squared"] = df["Area_SqFt"] ** 2

# age squared
df["Age_Squared"] = df["Property_Age"] ** 2

# log age
df["Log_Age"] = np.log1p(df["Property_Age"])

# area and age relationship
df["Area_Age"] = df["Area_SqFt"] * df["Property_Age"]

# area and bedrooms relationship
df["Area_Bedrooms"] = df["Area_SqFt"] * df["Bedrooms"]

# area and bathrooms relationship
df["Area_Bathrooms"] = df["Area_SqFt"] * df["Bathrooms"]

# area and floors relationship
df["Area_Floors"] = df["Area_SqFt"] * df["Floors"]

# garage and area relationship
df["Garage_Area"] = df["Garage"] * df["Area_SqFt"]

# age and bedrooms relationship
df["Age_Bedrooms"] = df["Property_Age"] * df["Bedrooms"]

# age and bathrooms relationship
df["Age_Bathrooms"] = df["Property_Age"] * df["Bathrooms"]

# city and property type
df["City_Property_Type"] = df["City"].astype(str) + "_" + df["Property_Type"].astype(str)

# city and condition
df["City_Condition"] = df["City"].astype(str) + "_" + df["Condition"].astype(str)

# location and property type
df["Location_Property_Type"] = df["Location"].astype(str) + "_" + df["Property_Type"].astype(str)

# relationship between numeric factors and price
print("\nNumeric Correlation with Price")

numeric_correlation = df.select_dtypes(include="number").drop(columns=["ID"],errors="ignore").corr()["Price_PKR"].sort_values(ascending=False)

print(numeric_correlation)

# relationship of area with price
print("\nArea and Price Relationship")
print("Area Correlation :",df["Area_SqFt"].corr(df["Price_PKR"]))

# relationship of bedrooms with price
print("\nBedrooms and Price Relationship")
print("Bedrooms Correlation :",df["Bedrooms"].corr(df["Price_PKR"]))

# relationship of bathrooms with price
print("\nBathrooms and Price Relationship")
print("Bathrooms Correlation :",df["Bathrooms"].corr(df["Price_PKR"]))

# relationship of year built with price
print("\nYear Built and Price Relationship")
print("Year Built Correlation :",df["Year_Built"].corr(df["Price_PKR"]))

# average price by city
print("\nAverage Price by City")
print(df.groupby("City")["Price_PKR"].agg(["count","mean","median"]).sort_values("median",ascending=False))

# average price by location
print("\nAverage Price by Location")
print(df.groupby("Location")["Price_PKR"].agg(["count","mean","median"]).sort_values("median",ascending=False))

# average price by property type
print("\nAverage Price by Property Type")
print(df.groupby("Property_Type")["Price_PKR"].agg(["count","mean","median"]).sort_values("median",ascending=False))

# average price by condition
print("\nAverage Price by Condition")
print(df.groupby("Condition")["Price_PKR"].agg(["count","mean","median"]).sort_values("median",ascending=False))

# one hot encoding
# convert categorical values into separate 0 and 1 columns
# this avoids giving categories a fake numerical order
df = pd.get_dummies(df,columns=df.select_dtypes(include="str").columns,dtype=int)

# check null values again
print("\nNull Values after cleaning :")
print(df.isnull().sum())

# split data 80/20 randomly
train,test = train_test_split(df,test_size=0.2,random_state=42)

print("\nTrain Shape :",train.shape)
print("Test Shape :",test.shape)

# save train and test
train.to_csv("train.csv",index=False)
test.to_csv("test.csv",index=False)

# factors
# select all columns except ID and Price_PKR
factors = df.columns.to_list()
factors.remove("ID")
factors.remove("Price_PKR")

print("\nNumber of Factors :",len(factors))

print("\nFactors :")
print(factors)

# split train into training and validation
train_part,validation = train_test_split(train,test_size=0.2,random_state=42)

print("\nTraining Part Shape :",train_part.shape)
print("Validation Shape :",validation.shape)

# standard scaling
scaler = StandardScaler()

train_part[factors] = scaler.fit_transform(train_part[factors])
validation[factors] = scaler.transform(validation[factors])

# train price
Y_train_part = np.log1p(train_part["Price_PKR"].values)

# ridge lambda values
lambda_values = [0.001,0.005,0.01,0.025,0.05,0.075,0.1,0.15,0.2,0.3,0.5,0.75,1]

best_lambda = None
best_validation_r2 = -np.inf

# test different lambda values
print("\nRidge Lambda Results")

for lambda_value in lambda_values:

    X_train_part = train_part[factors].values

    X_train_part = np.column_stack((np.ones(len(X_train_part)),X_train_part))

    X_transpose = X_train_part.T

    identity_matrix = np.eye(X_train_part.shape[1])

    # do not regularize intercept
    identity_matrix[0,0] = 0

    coefficients = np.linalg.pinv(X_transpose @ X_train_part + lambda_value * identity_matrix) @ X_transpose @ Y_train_part

    X_validation = validation[factors].values

    X_validation = np.column_stack((np.ones(len(X_validation)),X_validation))

    validation_predictions_log = X_validation @ coefficients

    validation_predictions = np.expm1(validation_predictions_log)

    validation_predictions = np.maximum(validation_predictions,0)

    validation_r2 = r2_score(validation["Price_PKR"],validation_predictions)

    print("Lambda :",lambda_value,"Validation R2 :",validation_r2)

    if validation_r2 > best_validation_r2:
        best_validation_r2 = validation_r2
        best_lambda = lambda_value

print("\nBest Lambda :",best_lambda)
print("Best Validation R2 :",best_validation_r2)

# standard scaling using complete training data
scaler = StandardScaler()

train[factors] = scaler.fit_transform(train[factors])
test[factors] = scaler.transform(test[factors])

# train price
Y_train = np.log1p(train["Price_PKR"].values)

# multiple linear regression
X_train = train[factors].values

# add column for intercept
X_train = np.column_stack((np.ones(len(X_train)),X_train))

# transpose
X_transpose = X_train.T

# ridge identity matrix
identity_matrix = np.eye(X_train.shape[1])

# do not regularize intercept
identity_matrix[0,0] = 0

# calculate coefficients
coefficients = np.linalg.pinv(X_transpose @ X_train + best_lambda * identity_matrix) @ X_transpose @ Y_train

# first coefficient is intercept
intercept = coefficients[0]

slopes = coefficients[1:]

print("\nIntercept :",intercept)

print("\nSlopes :")

for i in range(len(factors)):
    print(factors[i],"Slope m :",slopes[i])

# train predictions
X_train_prediction = np.column_stack((np.ones(len(train)),train[factors].values))

train_predictions_log = X_train_prediction @ coefficients

# convert log predictions back to PKR
train_predictions = np.expm1(train_predictions_log)

# prevent negative predictions
train_predictions = np.maximum(train_predictions,0)

# test predictions
X_test_prediction = np.column_stack((np.ones(len(test)),test[factors].values))

test_predictions_log = X_test_prediction @ coefficients

# convert log predictions back to PKR
test_predictions = np.expm1(test_predictions_log)

# prevent negative predictions
test_predictions = np.maximum(test_predictions,0)

# MAE
train_mae = mean_absolute_error(train["Price_PKR"],train_predictions)
test_mae = mean_absolute_error(test["Price_PKR"],test_predictions)

# MSE
train_mse = mean_squared_error(train["Price_PKR"],train_predictions)
test_mse = mean_squared_error(test["Price_PKR"],test_predictions)

# RMSE
train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)

# R2
train_r2 = r2_score(train["Price_PKR"],train_predictions)
test_r2 = r2_score(test["Price_PKR"],test_predictions)

print("\nTrain MAE :",train_mae)
print("Test MAE :",test_mae)

print("\nTrain MSE :",train_mse)
print("Test MSE :",test_mse)

print("\nTrain RMSE :",train_rmse)
print("Test RMSE :",test_rmse)

print("\nTrain R2 :",train_r2)
print("Test R2 :",test_r2)

print("\nBest Lambda :",best_lambda)

# first test house
print("\nFirst Test House")
print("Actual Price :",test["Price_PKR"].iloc[2])
print("Predicted Price :",test_predictions[2])