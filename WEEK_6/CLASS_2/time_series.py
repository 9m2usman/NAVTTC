import pandas as pd

df = pd.read_csv("./Datasets/shop_sales_daily.csv")
print(df.head())
df["date"] = pd.to_datetime(df["date"])
print(f"from {df['date'].min().date()} to {df['date'].max().date()} | {len(df)} days")

# pulll useful parts out of each dat
df["dayofweek"] = df["date"].dt.dayofweek #0-monday, 6-sunday
df["month"] = df["date"].dt.month

# look for patterns in the data
print(f"\nAveraege sales by day of week:")
print(df.groupby("dayofweek")["sales"].mean().round(2))
print(f"\nAverage sales by year:")
print(df.groupby(df["date"].dt.year)["sales"].mean().round(2))


# lag features time split base line
import pandas as pd
from sklearn.metrics import mean_squared_error

df = pd.read_csv("shop_sales_daily.csv", parse_dates=["date"])
# lag features the past becomes the input
df["lag_1"] = df["sales"].shift(1) #yesterday's sales becomes today's input
df["lag_7"] = df["sales"].shift(7) #same day last week becomes today's input
df['roll_7'] = df['sales'].shift(1).rolling(7).mean() #last 7 days average becomes today's input
df['dayofweek'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month
df = df.dropna() #drop the first 7 rows that have no lag features

# split by time, not random, to avoid data leakage
train = df[df['date'] < '2025-10-01']
test = df[df['date'] >= '2025-10-01']
print(f"train days {len(train)} | test days {len(test)}")

# baselines: simple guesses every model must beat
for name,col in [("naive yesterday's sales", "lag_1"), ("seasonal naive (lag_7)", "lag_7"), ("last 7 days average", "roll_7")]:
    print(f"{name:24s} MAE | {mean_squared_error(test['sales'], test[col]):.1f}")

# continue from code 2 df train and test already built
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("./Datasets/shop_sales_daily.csv", parse_dates=["date"])
# lag features the past becomes the input
df["lag_1"] = df["sales"].shift(1) #yesterday's sales becomes today's input
df["lag_7"] = df["sales"].shift(7) #same day last week becomes today's input
df["roll_7"] = df["sales"].shift(1).rolling(7).mean() #last 7 days average becomes today's input
df["dayofweek"] = df["date"].dt.dayofweek
df["month"] = df["date"].dt.month
df = df.dropna() #drop the first 7 rows that have no lag features

# split by time, not random, to avoid data leakage
train = df[df['date'] < '2025-10-01']
test = df[df['date'] >= '2025-10-01']

features = ["lag_1","lag_7","roll_7","dayofweek","month"]
x_train,x_test,y_train,y_test = train[features],test[features],train["sales"],test["sales"]

for name, model in [("Linear Regression", LinearRegression()),("Random Forest", RandomForestRegressor(n_estimators=300, random_state=42))]:
    model.fit(x_train,y_train)
    pred = model.predict(x_test)
    print(f"{name:18s} MAE | {mean_absolute_error(y_test, pred):.1f}")

# which past value help the most? feature importance for random forest
rf = RandomForestRegressor(300, random_state=42).fit(x_train,y_train)
print(pd.Series(rf.feature_importances_, index=features).round(2))
