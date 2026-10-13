# multi & poly = x,x**2,x**3...x**n this polynomial and in polynomial we have degree and in graph we have curve
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# load ready mode dataset already cleaned
df = pd.read_csv("students_week5.csv")
features = ['study_hours', 'attendance_pct', 'previous_score',
       'sleep_hours', 'assignments_done', 'internet_access', 'extra_tuition',
       'part_time_job', 'parent_education']

x = df[features]
y = df['final_score']

#split train and predict
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
model = LinearRegression()
model.fit(x_train,y_train)
pred = model.predict(x_test)

# evaluate + see what the model learned
print("R2 : ",round(r2_score(y_test,pred),3))
print("RMSE : ",round(mean_squared_error(y_test,pred)**0.5,2))
print(pd.Series(model.coef_,index=features).round(2))

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("students_week5.csv")
x = df.drop(columns=['student_id','final_score','result','performance'])
y = df['final_score']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=10) #its not gonna shuffle same as always 

degrees = []
train_r2_values = []
test_r2_values = []

# try degree 1, degree2 , degree3 --- watch train vs test score
for degree in range(1,10):
    model = make_pipeline(PolynomialFeatures(degree),LinearRegression())
    model.fit(x_train,y_train)

    train_r2 = r2_score(y_train,model.predict(x_train))
    test_r2 = r2_score(y_test,model.predict(x_test))

    degrees.append(degree)
    train_r2_values.append(train_r2)
    test_r2_values.append(test_r2)

    print(f"Degree {degree}: train r2 = {train_r2:.3f} | test r2 = {test_r2:.3f}")

plt.plot(degrees,train_r2_values,marker="o",label="Train R2")
plt.plot(degrees,test_r2_values,marker="o",label="Test R2")

plt.xlabel("Polynomial Degree")
plt.ylabel("R2 Score")
plt.title("Polynomial Degree vs R2 Score")
plt.legend()
plt.show()

