# feature engineering
import pandas as pd
df = pd.DataFrame({
    "height_cm":[170,179,160],
    "weight_kg":[65,80,55]
})
df["bmi"] = df["weight_kg"]/(df["height_cm"]/100)**2
print(df)

# form dataset price and quantity col crete a new total cost feature
df2 = pd.DataFrame({
    "price":[20,30,40],
    "quantity":[10,20,30]
})
df2["total_price"] = df2["price"]*df2["quantity"]
print(df2)

# from total_income and toal_expense col engineer savings rate features (savings/income)
df3 = pd.DataFrame({
    "total_income" : [330,430,220],
    "total_expense" : [230,410,200]
})
df3["saving_rates"] = (( df3["total_income"] - df3["total_expense"] ) / ( df3["total_income"] ) ) * 100
print(df3)

# feature selection and binning
# binning(discretization) : groups continuous values into category, e.g. turning exact age into age vrackets.
import pandas as pd
df = pd.DataFrame({
    "study_hours" : [1,2,3,4,5],
    "sleep_hoours" : [8,7,6,8,7],
    "marks" : [50,55,60,70,85]
})
print(df.corr()["marks"])
ages = pd.Series([5,17,25,45,68,80])
print(pd.cut(ages, bins=[0,12,19,59,100], # bins = (0-12  value = child)  (12-19 value teen) (19-59 value adult) (59-100 value senior)
             labels=["child","teen","adult","senior"])) #now here it matches the ages which is given above and find where it lies

# compute cor 3 numeric col against a target col - which feature least useful
df = pd.DataFrame({
    "student_attendace" : [1,2,3,4,5],
    "student_focus" : [3,2,3,4,5],
    "teaacher_evaluation" : [50,55,60,70,85],
    "student_marks" : [8,7,6,8,7],
})
print(df.corr()["student_marks"])
# here most useless one is teacher evaluation

# bin a col of exam score 0-100 into fail pass merit distinction categories using pd.cut()
marks = pd.Series([5,17,25,45,68,80])
print(pd.cut(ages, bins=[0,33,50,69,100], # bins = (0-12  value = child)  (12-19 value teen) (19-59 value adult) (59-100 value senior)
             labels=["fail","pass","merit","distinction"])) #now here it matches the ages which is given above and find where it lies

# etl(extraction,transformation,load) & batch vs stream processing
#OLTP online transaction processing = quick transaction & OLAP online analytical processing 2 important experts

# elt example - conceptual
#extract : read raw sales data from a csv/database

raw = pd.read_csv("daily_sales.csv")

# automation with sklearn pipelines
# pipelines do first thing then do second and then do third it will automatically do one,2nd,3rd

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np

#data - study hours vs exam score
X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]]) #marks
Y = np.array([40,45,52,60,68,75,82,90]) #exa score

pipe = Pipeline([
    ("Scaler",StandardScaler()),
    ("model",LinearRegression())
])
pipe.fit(X,Y)
print(pipe.predict([[9]]))
print(pipe.predict([[9],[11]]).astype(int))

X1 = np.array([[20],[40],[30],[58],[53],[68],[72],[82]]) #money
Y1 = np.array([400,800,600,1160,1060,1360,1440,1640]) #shoes
pipe.fit(X1,Y1)
print(pipe.predict([[33]]))