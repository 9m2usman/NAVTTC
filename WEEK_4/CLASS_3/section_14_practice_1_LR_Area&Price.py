import pandas as pd

df = pd.read_csv("./Datasets/housing.csv")

print(df)

# Convert Area from square feet to Marla
df["Area"] = df["Area"] / 272.25

print(df.columns.to_list())

col_list = df.columns.to_list()

not_need_col = []

for col in col_list:

    if col != "Area" and col != "Price":
        not_need_col.append(col)

df = df.drop(columns=not_need_col)
split = int(len(df) * 0.8)

df1 = df.iloc[split:]   # 20%
df2 = df.iloc[:split]   # 80%

df1.to_csv("housing_test.csv",index = False)
df2.to_csv("housing_train.csv",index = False)

train = pd.read_csv("housing_test.csv")

# mean of train area
area_mean = sum(train["Area"])/len(train)
print("mean area : ",area_mean)

# mean of train price
price_mean = sum(train["Price"])/len(train)
print("mean price",price_mean)


# dev(x), dev(y), dev(x)*dev(y), [dev(x)]**2
dev_x = []
dev_y = []
product_dev = []
square_dev_x = []

for i in range(len(train)):
    dx = train["Area"][i] - area_mean
    dy = train["Price"][i] - price_mean
    product = dx * dy
    square = dx**2
    dev_x.append(dx)
    dev_y.append(dy)
    product_dev.append(product)
    square_dev_x.append(square)


slope = sum(product_dev) / sum(square_dev_x)
print("Slope m : ",slope)
intercept = price_mean - (slope * area_mean)
print("a constant/intercept/weight : ",intercept)

train["Price"] = slope*(train["Area"]) + intercept


# training done now move to testing phase..
test = pd.read_csv("housing_test.csv")
test["Price"][0] = int(slope*(test["Area"][0]) + intercept)
print(test["Price"][0])
