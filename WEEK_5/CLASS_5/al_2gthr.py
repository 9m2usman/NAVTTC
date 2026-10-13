import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,confusion_matrix)

# STEP 1 - EXTRACT DATA
df = pd.read_csv("./Datasets/Titanic-Dataset.csv")
print(df.shape)
print(df.isnull().sum())

# STEP 2 - TRANSFORM DATA
df["Title"] = df["Name"].str.extract(r",\s*([^.]+)\.", expand=False)
print("<====== Title Now ========>",df["Title"]) 
df["Title"] = df["Title"].str.strip()
df["Title"] = df["Title"].replace({"Mlle": "Miss","Ms": "Miss","Mme": "Mrs"})
common_titles = ["Mr", "Miss", "Mrs", "Master"]
df.loc[~df["Title"].isin(common_titles), "Title"] = "Other"
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)
df["HasCabin"] = df["Cabin"].notna().astype(int)
df["CabinDeck"] = df["Cabin"].str[0]
df["FarePerPerson"] = df["Fare"] / df["FamilySize"]
df["LogFare"] = np.log1p(df["Fare"])
df["TicketGroupSize"] = df.groupby("Ticket")["Ticket"].transform("count")
df["Child"] = (df["Age"] < 16).astype(int)
df["Mother"] = ( (df["Sex"] == "female") & (df["Parch"] > 0) & (df["Age"] > 18) & (df["Title"] == "Mrs") ).astype(int)
df["FamilyGroup"] = pd.cut( df["FamilySize"], bins=[0, 1, 4, 7, 20], labels=["Alone", "Small", "Medium", "Large"] )

# STEP 3 - REMOVE UNNECESSARY COLUMNS
df = df.drop(columns=["PassengerId","Name","Ticket","Cabin" ])

# STEP 4 - INPUT AND OUTPUT
X = df.drop(columns=["Survived"])
y = df["Survived"]

# STEP 5 - TRAIN TEST SPLIT
train_x, test_x, train_y, test_y = train_test_split(X,y,test_size=0.20,random_state=42,stratify=y)

# STEP 6 - FEATURES
numerical_features = ["Age","Fare","FarePerPerson","LogFare","SibSp","Parch","Pclass","FamilySize","TicketGroupSize","IsAlone","HasCabin","Child","Mother"]
categorical_features = ["Sex","Embarked","Title","CabinDeck","FamilyGroup"]

# STEP 7 - PREPROCESSING PIPELINE
numerical_pipeline = Pipeline([ ("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler()) ])
categorical_pipeline = Pipeline([ ("imputer", SimpleImputer(strategy="most_frequent")),("encoder", OneHotEncoder(handle_unknown="ignore",sparse_output=False)) ])
preprocessor = ColumnTransformer([("numerical", numerical_pipeline, numerical_features),("categorical", categorical_pipeline, categorical_features) ])

# STEP 8 - MODELS AND PARAMETERS
models = {
    "Logistic Regression": ( LogisticRegression(max_iter=3000), { "model__C": [0.01, 0.1, 1, 10, 100], "model__solver": ["liblinear", "lbfgs"], "model__class_weight": [None, "balanced"] }),
    "SVM (RBF)": (SVC(probability=True,random_state=42),{"model__C": [0.1, 1, 10, 50, 100],"model__gamma": ["scale", 0.001, 0.01, 0.1],"model__class_weight": [None, "balanced"]}),
    "Gaussian Naive Bayes": (GaussianNB(),{"model__var_smoothing": [1e-11,1e-10,1e-9,1e-8,1e-7,1e-6]}),
    "KNN": (KNeighborsClassifier(),{"model__n_neighbors": [3, 5, 7, 9, 11, 15, 21],"model__weights": ["uniform", "distance"],"model__p": [1, 2]})
}

# STEP 9 - TRAIN AND TEST MODELS
results = []
confusion_matrices = {}
for model_name in models:
    model_algorithm = models[model_name][0]
    parameters = models[model_name][1]
    pipeline = Pipeline([("preprocessor", preprocessor),("model", model_algorithm)])
    grid = GridSearchCV(pipeline,parameters,cv=5,scoring="accuracy",n_jobs=-1)
    grid.fit(train_x, train_y)
    prediction = grid.predict(test_x)
    probability = grid.predict_proba(test_x)[:, 1]
    accuracy = accuracy_score(test_y, prediction)
    precision = precision_score(test_y,prediction,zero_division=0)
    recall = recall_score(test_y,prediction,zero_division=0)
    f1 = f1_score(test_y,prediction,zero_division=0)
    auc = roc_auc_score(test_y,probability)

    results.append({"Model": model_name,"Accuracy": accuracy,"Precision": precision,"Recall": recall,"F1": f1,"ROC-AUC": auc})
    confusion_matrices[model_name] = confusion_matrix(test_y,prediction)
    print("\n", model_name)
    print("Best Parameters:", grid.best_params_)
    print(f"Accuracy  : {accuracy:.3f}")
    print(f"Precision : {precision:.3f}")
    print(f"Recall    : {recall:.3f}")
    print(f"F1 Score  : {f1:.3f}")
    print(f"ROC-AUC   : {auc:.3f}")

# STEP 10 - FINAL ACCURACY OF ALL MODELS
results_df = pd.DataFrame(results)
results_df = results_df.sort_values("Accuracy",ascending=False)
print("\nFINAL ACCURACY OF ALL MODELS")
print(results_df[["Model", "Accuracy"]].round(3).to_string(index=False))

# STEP 11 - HIGHEST ACCURACY FROM EACH MODEL
print("\nHIGHEST ACCURACY FROM EACH MODEL")
for index in results_df.index:
    print(f"{results_df.loc[index, 'Model']} : \n{results_df.loc[index, 'Accuracy']:.3f}")

# STEP 12 - COMPLETE MODEL COMPARISON
print("\nCOMPLETE MODEL COMPARISON")
print(results_df.round(3).to_string(index=False))

# STEP 13 - ACCURACY GRAPH
plt.figure(figsize=(9, 5))
plt.bar(results_df["Model"],results_df["Accuracy"])
plt.ylim(0, 1)
plt.ylabel("Accuracy")
plt.title("Titanic Model Accuracy")
plt.xticks(rotation=20,ha="right")
plt.tight_layout()
plt.show()

# STEP 14 - ALL METRICS GRAPH
metrics = ["Accuracy","Precision","Recall","F1","ROC-AUC"]
results_df.set_index("Model")[metrics].plot(kind="bar",figsize=(10, 6))
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("Titanic Model Performance")
plt.xticks(rotation=20,ha="right")
plt.tight_layout()
plt.show()

# STEP 15 - CONFUSION MATRICES
for model_name in confusion_matrices:
    print(f"\nConfusion Matrix - {model_name}")
    print(confusion_matrices[model_name])
    plt.figure(figsize=(5, 4))
    plt.imshow(confusion_matrices[model_name])
    plt.title(f"Confusion Matrix - {model_name}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.colorbar()
    plt.xticks([0, 1],["Not Survived", "Survived"])
    plt.yticks([0, 1],["Not Survived", "Survived"])
    plt.tight_layout()
    plt.show()
