import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
path = os.path.abspath("Books_Data_Clean.csv")
df = pd.read_csv(path)

# row ans col
print(df.shape)

# missig vlaue and how many in col
print(df.isnull().sum())

# book avr_rating across all books
print(df.groupby("Book Name")["Book_average_rating"].mean().head(10))

# total gross sale across all books(sum,not_avg)
print(df.groupby("Book Name")["gross sales"].sum().head(10))

# what genre appears most frequently in dataset
print(df["genre"].value_counts())

# publisher highest total unit sold
print(df.groupby("Publisher ")["units sold"].value_counts())
print(df.groupby("Publisher ")["units sold"].value_counts().idxmax(),df.groupby("Publisher ")["units sold"].value_counts().max())

# cor between gross sales and publisher revenue
print(df["gross sales"].corr(df["publisher revenue"]))

# investigate :sort dataset from smallest to largest do u notice anything unsual about the smallest values? investigate rows what books are they?
print(df["Publishing Year"].sort_values(), "\nsorted values")
sorted_values = df.sort_values("Publishing Year")


# handle missing val you found in round 1,Decide stratergy in each colmn and justify it in a commnet
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("Books_Data_Clean.csv")

# Clean column names
df.columns = df.columns.str.strip()
# Separate numeric and categorical columns
numeric_columns = df.select_dtypes(include="number").columns
categorical_columns = df.select_dtypes(include="str").columns
print(numeric_columns)
print(categorical_columns)
# Check missing values
print(df[numeric_columns].isnull().sum())
print(df[categorical_columns].isnull().sum())
# Handle missing numeric value
df["Publishing Year"] = df["Publishing Year"].fillna(df["Publishing Year"].median())
# Handle categorical columns
for categorical_column in categorical_columns:
    df[categorical_column] = (df[categorical_column].fillna("unknown").str.strip())

# he genre col has 4 category apply one hot encoding it it and print th result

#the autho rating column has a natural order novice<intermediate<excellent<famous apply lable encoding to the num respect this order
import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("Books_Data_Clean.csv")
le = LabelEncoder()
print(le.fit_transform(df["Author_Rating"]))
# another mehtod
unique_ratings = df["Author_Rating"].unique()
encoding = le.fit_transform(unique_ratings)
#use for loop for representing both 
for i in range(len(unique_ratings)):
    print("(",unique_ratings[i], "->", encoding[i],"),",end="")
print()

#or use zip method for its representation of both
for name, value in zip(unique_ratings, encoding):
    print(name, "=", value)

# check skewness of gross_sale apply transform of log and then chck skewness again did it change.
import pandas as pd
import numpy as np
df = pd.read_csv("Books_Data_Clean.csv")

skewness = df["gross sales"].skew()
print("Original Skewness",skewness)

log_gross_sales = np.log(df["gross sales"])
log_skewness = log_gross_sales.skew()
print("Log skewness",log_skewness)

# apply standard scale to the unit sold vol confrim the transform mean is approx 0
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
df = pd.read_csv("Books_Data_Clean.csv")
ss = StandardScaler()
mms = MinMaxScaler()
print(ss.fit_transform(df[["units sold"]]).flatten(),mms.fit_transform(df[["units sold"]]).flatten())
print("Mean value of transfrom units sols",ss.fit_transform(df[["units sold"]]).flatten().mean())
