import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report

df = pd.read_csv("./Datasets/students_week5.csv")
x = df.drop(columns=['student_id','final_score','result','performance'])
y = df['result'] # 1-> pass , 0 -> fail
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42, stratify=y)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)
pred = model.predict(x_test)
print("Accurace : ",accuracy_score(y_test,pred))
print("Confusion Matrix : \n",confusion_matrix(y_test,pred))
print("Classification Report : \n",classification_report(y_test,pred))

# #
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report

df = pd.read_csv("./Datasets/students_week5.csv")
x = df.drop(columns=['student_id','final_score','result','performance'])
y = df['performance'] # 2 -> high ,1-> medium , 0 -> low
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42, stratify=y)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)
pred = model.predict(x_test)
print("Accurace : ",accuracy_score(y_test,pred))
print("Confusion Matrix : \n",confusion_matrix(y_test,pred))
print("Classification Report : \n",classification_report(y_test,pred))
print("Probability : ",model.predict_proba(x_test[:3]).round(2)) #probablity of each class
 