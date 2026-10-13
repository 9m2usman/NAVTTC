import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

df = pd.read_csv("./Datasets/breast_cancer.csv")
print(df.head(),df.shape,df.columns)

df = df.drop(columns=['id', 'Unnamed: 32'])  # Drop unnecessary columns
x = df.drop(columns=['diagnosis'])  
y = df['diagnosis']

train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)
models = {'Logistic Regression': LogisticRegression(max_iter=1000),
          'SVM (rbf)': SVC(kernel='rbf'),
          'SVM (linear)': SVC(kernel='linear'),
          'Naive Bayes': GaussianNB(),
          'KNN': KNeighborsClassifier(n_neighbors=5)}

prediction = {}

for model in range(len(models)):
    model_name = list(models.keys())[model]
    model = list(models.values())[model]
    model.fit(train_x,train_y)
    prediction[model_name] = model.predict(test_x)
    acc = accuracy_score(test_y,prediction[model_name])
    print(f"{model_name} : Accuracy = {acc:.3f}")

