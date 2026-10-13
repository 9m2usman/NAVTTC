import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# STEP 1 - EXTRACT DATA FROM ONLINE SOURCE
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
data = pd.read_csv(url, sep="\t", header=None, names=["label", "message"])
print("Original Data")
print(data.head())
print()
print("Shape:", data.shape)
print()

# STEP 2 - CHECK DATA
print("Missing Values")
print(data.isnull().sum())
print()
print("Duplicate Rows:", data.duplicated().sum())
print()
print("Labels")
print(data["label"].value_counts())
print()

# STEP 3 - REMOVE DUPLICATES
data = data.drop_duplicates().reset_index(drop=True)
print("After Removing Duplicates")
print("Shape:", data.shape)
print()

# STEP 4 - TRANSFORM LABEL
data["label"] = data["label"].replace({"ham": 0,"spam": 1})
print("After Label Transformation")
print(data.head())
print()

# STEP 5 - CREATE FEATURES
data["message_length"] = data["message"].str.len()
data["word_count"] = data["message"].str.split().str.len()
data["digit_count"] = data["message"].str.count(r"\d")
data["exclamation_count"] = data["message"].str.count("!")
data["dollar_count"] = data["message"].str.count(r"\$")
data["question_count"] = data["message"].str.count(r"\?")
data["capital_count"] = data["message"].str.count(r"[A-Z]")

# STEP 6 - CREATE URL FEATURE
data["url_count"] = data["message"].str.count("http")
print("Features Created")
print(data.head())
print()

# STEP 7 - LOAD TRANSFORMED DATA
data.to_csv("spam_transformed.csv", index=False)
data = pd.read_csv("spam_transformed.csv")
print("Transformed Data Loaded Again")
print(data.head())
print()

# STEP 8 - SELECT X AND Y
x = data[ ["message_length","word_count","digit_count","exclamation_count","dollar_count","question_count","capital_count","url_count"] ]
y = data["label"]
print("X Shape:", x.shape)
print("Y Shape:", y.shape)
print()

# STEP 9 - TRAIN TEST SPLIT
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
print("Training Data:", x_train.shape)
print("Testing Data:", x_test.shape)
print()

# STEP 10 - TRAIN SVM MODELS
kernels = ["linear", "rbf"]
models = {}
predictions = {}
confusion_matrices = {}
accuracy = {}
precision = {}
recall = {}
f1 = {}

for kernel in kernels:
    print("SVM", kernel.upper())
    model = SVC(kernel=kernel)
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    models[kernel] = model
    predictions[kernel] = prediction
    accuracy[kernel] = accuracy_score(y_test, prediction)
    precision[kernel] = precision_score(y_test, prediction)
    recall[kernel] = recall_score(y_test, prediction)
    f1[kernel] = f1_score(y_test, prediction)
    confusion_matrices[kernel] = confusion_matrix(y_test,prediction)
    print("Accuracy:", round(accuracy[kernel], 3))
    print("Precision:", round(precision[kernel], 3))
    print("Recall:", round(recall[kernel], 3))
    print("F1 Score:", round(f1[kernel], 3))
    print()
    print("Confusion Matrix")
    print(confusion_matrices[kernel])
    print()

# STEP 11 - TEST A NEW MESSAGE
new_message = "http://Congratulations! You have won a free prize! Call now!"
new_message_features = np.array([ [
        len(new_message),
        len(new_message.split()),
        sum(char.isdigit() for char in new_message),
        new_message.count("!"),
        new_message.count("$"),
        new_message.count("?"),
        sum(char.isupper() for char in new_message),
        new_message.count("http")
    ] ])
for kernel in kernels:
    new_prediction = models[kernel].predict(new_message_features)
    print("MODEL:", kernel.upper())
    print("NEW MESSAGE")
    print(new_message)
    if new_prediction[0] == 1:
        print("Prediction: SPAM")
    else:
        print("Prediction: HAM")
    print()

# STEP 12 - CLASS DISTRIBUTION GRAPH
label_counts = data["label"].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(
    ["HAM", "SPAM"],
    [label_counts.get(0, 0), label_counts.get(1, 0)] )
plt.title("Spam vs Ham Messages")
plt.xlabel("Message Type")
plt.ylabel("Number of Messages")
plt.show()

# STEP 13 - CONFUSION MATRIX GRAPHS
for kernel in kernels:
    cm = confusion_matrices[kernel]
    plt.figure(figsize=(5, 4))
    plt.imshow(cm)
    plt.title(kernel.upper() + " SVM Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.xticks( [0, 1],["HAM", "SPAM"] )
    plt.yticks( [0, 1],["HAM", "SPAM"] )
    for i in range(2):
        for j in range(2):
            plt.text(j,i,cm[i, j],ha="center",va="center")
    plt.show()

# STEP 14 - MODEL COMPARISON
print("MODEL COMPARISON")
print()
for kernel in kernels:
    print(kernel.upper(), "SVM")
    print("Accuracy:", round(accuracy[kernel], 3))
    print("Precision:", round(precision[kernel], 3))
    print("Recall:", round(recall[kernel], 3))
    print("F1 Score:", round(f1[kernel], 3))
    print()

