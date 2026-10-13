import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("./Datasets/students_week5.csv")
x = df.drop(columns = ["student_id","final_score","performance","result"])
y = df["result"]
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
y1 = (df["performance"] == 2).astype(int)  # 1 = good, 0 = average/bad
print(f"share of high performance {y1.mean():.2%}")

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)
x_train,x_test,y1_train,y1_test = train_test_split(x,y1,test_size=0.2,random_state=42,stratify=y1)

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
model.fit(x_train,y_train)

prob = model.predict_proba(x_test)[:,1] #chances of pass
for threshold in [0.5,0.3,0.7]:
    pred = (prob >= threshold).astype(int) #our own cut off
    print(f"threshold {threshold}\nprecision score : {precision_score(y_test,pred):.2f}\nrecall : {recall_score(y_test,pred):.2f}\nf1_score : {f1_score(y_test,pred):.2f}")
print(f"roc_auc_score : {roc_auc_score(y_test,prob):.2f}")
print(f"confusion_matrix : {confusion_matrix(y_test,pred)}")

models = { "Dummy": DummyClassifier(strategy="most_frequent"),
    "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)),
    "Logistic Regression Balanced": make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000,class_weight="balanced"))}

for name,m in models.items():
    pred = m.fit(x_train,y_train).predict(x_test)
    print(f"{name} : precision score : {precision_score(y1_test,pred):.2f}\nrecall : {recall_score(y1_test,pred):.2f}\nf1_score : {f1_score(y1_test,pred):.2f}\naccuracy_score : {accuracy_score(y1_test,pred)}")

# cross_validation 5 practice test on train data only
scores = cross_val_score(make_pipeline(StandardScaler(),SVC()), x_train, y_train, cv=cv)
print(f"SVM 5 Scores : {scores.round(3)}\nmean : {scores.mean():.2f}")

# grid search cv try everything keep best cv score
settings = {"max_depth":[2,3,4,5,6,8],"min_samples_leaf":[1,5,10,20]}
grid = GridSearchCV(DecisionTreeClassifier(random_state=42), settings, cv=cv)
grid.fit(x_train,y_train)
print(f"Best {grid.best_params_}\nCV{grid.best_score_:.2f}\nfinal test score : {grid.score(x_test,y_test):.2f}")