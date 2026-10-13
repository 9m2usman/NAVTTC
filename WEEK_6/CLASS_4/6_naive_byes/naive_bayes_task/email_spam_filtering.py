import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# STEP 1 - EXTRACT DATA FROM ONLINE SOURCE
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
data = pd.read_csv(url, sep="\t", header=None, names=["label", "message"])
print(data.head())
print(data.shape)

# STEP 2 - CLEAN DATA
data["label"] = data["label"].map({"ham": 0, "spam": 1})
data = data.dropna()
data = data.drop_duplicates()
print(data.isnull().sum())
print(data.duplicated().sum())

# STEP 3 - CREATE NUMERICAL FEATURES
data["message_length"] = data["message"].str.len()
data["word_count"] = data["message"].str.split().str.len()
data["digit_count"] = data["message"].str.count(r"\d")
data["exclamation_count"] = data["message"].str.count("!")
data["capital_count"] = data["message"].str.count(r"[A-Z]")
data["question_count"] = data["message"].str.count(r"\?")

# STEP 4 - SELECT NUMERICAL FEATURES
X = data[[ "message_length","word_count","digit_count","exclamation_count","capital_count","question_count" ]]
y = data["label"]

# STEP 5 - TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# STEP 6 - DATA SCALING

# StandardScaler is useful for GaussianNB and SVM.
# It creates negative values after scaling.
# Therefore, these scaled values cannot be directly used
# with MultinomialNB.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# STEP 7 - TRAIN GAUSSIAN NAIVE BAYES
gnb_model = GaussianNB()
gnb_model.fit(X_train_scaled, y_train)

# STEP 8 - GAUSSIAN NB PREDICTION
gnb_pred = gnb_model.predict(X_test_scaled)

# STEP 9 - GAUSSIAN NB EVALUATION
gnb_accuracy = accuracy_score(y_test, gnb_pred)
gnb_precision = precision_score(y_test, gnb_pred)
gnb_recall = recall_score(y_test, gnb_pred)
gnb_f1 = f1_score(y_test, gnb_pred)
print("GaussianNB Accuracy:", round(gnb_accuracy, 3))
print("GaussianNB Precision:", round(gnb_precision, 3))
print("GaussianNB Recall:", round(gnb_recall, 3))
print("GaussianNB F1 Score:", round(gnb_f1, 3))

# STEP 10 - GAUSSIAN NB CONFUSION MATRIX
gnb_cm = confusion_matrix(y_test, gnb_pred)
print("GaussianNB Confusion Matrix:")
print(gnb_cm)

# STEP 11 - TRAIN SVM
# SVM can also work well with scaled numerical features.
svm_model = SVC(kernel="linear", probability=True)
svm_model.fit(X_train_scaled, y_train)

# STEP 12 - SVM PREDICTION
svm_pred = svm_model.predict(X_test_scaled)


# STEP 13 - SVM EVALUATION
svm_accuracy = accuracy_score(y_test, svm_pred)
svm_precision = precision_score(y_test, svm_pred)
svm_recall = recall_score(y_test, svm_pred)
svm_f1 = f1_score(y_test, svm_pred)
print("SVM Accuracy:", round(svm_accuracy, 3))
print("SVM Precision:", round(svm_precision, 3))
print("SVM Recall:", round(svm_recall, 3))
print("SVM F1 Score:", round(svm_f1, 3))

# STEP 14 - SVM CONFUSION MATRIX
svm_cm = confusion_matrix(y_test, svm_pred)
print("SVM Confusion Matrix:")
print(svm_cm)

# STEP 15 - MULTINOMIAL NB USING YOUR NUMERICAL FEATURES

# MultinomialNB requires non-negative values.
# We do NOT use StandardScaler here because StandardScaler
# produces negative values.
#
# Your original numerical features are already non-negative.
# Therefore, we use the original X_train and X_test directly.
mnb_model = MultinomialNB()
mnb_model.fit(X_train, y_train)

# STEP 16 - MULTINOMIAL NB PREDICTION
mnb_pred = mnb_model.predict(X_test)

# STEP 17 - MULTINOMIAL NB EVALUATION
mnb_accuracy = accuracy_score(y_test, mnb_pred)
mnb_precision = precision_score(y_test, mnb_pred)
mnb_recall = recall_score(y_test, mnb_pred)
mnb_f1 = f1_score(y_test, mnb_pred)
print("MultinomialNB Numerical Accuracy:", round(mnb_accuracy, 3))
print("MultinomialNB Numerical Precision:", round(mnb_precision, 3))
print("MultinomialNB Numerical Recall:", round(mnb_recall, 3))
print("MultinomialNB Numerical F1 Score:", round(mnb_f1, 3))

# STEP 18 - MULTINOMIAL NB NUMERICAL CONFUSION MATRIX
mnb_cm = confusion_matrix(y_test, mnb_pred)
print("MultinomialNB Numerical Confusion Matrix:")
print(mnb_cm)

# STEP 19 - TEXT VECTORIZATION

# This is the second method.
#
# Instead of manually creating features such as message_length
# and word_count, TfidfVectorizer converts the actual message
# text into numerical features.
#
# TF-IDF produces non-negative values, so it is suitable
# for MultinomialNB.
text_vectorizer = TfidfVectorizer()
X_text = text_vectorizer.fit_transform(data["message"])
y_text = data["label"]


# STEP 20 - TEXT TRAIN TEST SPLIT
X_text_train, X_text_test, y_text_train, y_text_test = train_test_split(X_text,y_text,test_size=0.2,random_state=42)

# STEP 21 - TRAIN MULTINOMIAL NB WITH TF-IDF
mnb_text_model = MultinomialNB()
mnb_text_model.fit(X_text_train, y_text_train)

# STEP 22 - MULTINOMIAL NB TF-IDF PREDICTION
mnb_text_pred = mnb_text_model.predict(X_text_test)

# STEP 23 - MULTINOMIAL NB TF-IDF EVALUATION
mnb_text_accuracy = accuracy_score(y_text_test, mnb_text_pred)
mnb_text_precision = precision_score(y_text_test, mnb_text_pred)
mnb_text_recall = recall_score(y_text_test, mnb_text_pred)
mnb_text_f1 = f1_score(y_text_test, mnb_text_pred)
print("MultinomialNB TF-IDF Accuracy:", round(mnb_text_accuracy, 3))
print("MultinomialNB TF-IDF Precision:", round(mnb_text_precision, 3))
print("MultinomialNB TF-IDF Recall:", round(mnb_text_recall, 3))
print("MultinomialNB TF-IDF F1 Score:", round(mnb_text_f1, 3))

# STEP 24 - MULTINOMIAL NB TF-IDF CONFUSION MATRIX
mnb_text_cm = confusion_matrix(y_text_test, mnb_text_pred)
print("MultinomialNB TF-IDF Confusion Matrix:")
print(mnb_text_cm)

# STEP 25 - COMPARE ALL MODELS
comparison = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
    "GaussianNB": [gnb_accuracy,gnb_precision,gnb_recall,gnb_f1],
    "SVM": [svm_accuracy,svm_precision,svm_recall,svm_f1],
    "MultinomialNB Numerical": [mnb_accuracy,mnb_precision,mnb_recall,mnb_f1],
    "MultinomialNB TF-IDF": [mnb_text_accuracy,mnb_text_precision,mnb_text_recall,mnb_text_f1]
})
print("\nFINAL MODEL COMPARISON")
print(comparison)

# STEP 26 - NEW MESSAGE USING YOUR NUMERICAL METHOD
new_message = pd.DataFrame({
    "message_length": [180],
    "word_count": [35],
    "digit_count": [15],
    "exclamation_count": [6],
    "capital_count": [30],
    "question_count": [1]
})

# STEP 27 - SCALE NEW MESSAGE
new_message_scaled = scaler.transform(new_message)

# STEP 28 - GAUSSIAN NB NEW PREDICTION
gnb_prediction = gnb_model.predict(new_message_scaled)
gnb_probability = gnb_model.predict_proba(new_message_scaled)
print("\nGaussianNB Prediction:", gnb_prediction[0])
print("GaussianNB Probability:", gnb_probability[0])
if gnb_prediction[0] == 1:
    print("GaussianNB Result: Spam")
else:
    print("GaussianNB Result: Not Spam")

# STEP 29 - SVM NEW PREDICTION
svm_prediction = svm_model.predict(new_message_scaled)
svm_probability = svm_model.predict_proba(new_message_scaled)
print("SVM Prediction:", svm_prediction[0])
print("SVM Probability:", svm_probability[0])
if svm_prediction[0] == 1:
    print("SVM Result: Spam")
else:
    print("SVM Result: Not Spam")

# STEP 30 - MULTINOMIAL NB NUMERICAL NEW PREDICTION
# MultinomialNB uses the original non-scaled numerical features.
mnb_prediction = mnb_model.predict(new_message)
mnb_probability = mnb_model.predict_proba(new_message)
print("MultinomialNB Numerical Prediction:", mnb_prediction[0])
print("MultinomialNB Numerical Probability:", mnb_probability[0])
if mnb_prediction[0] == 1:
    print("MultinomialNB Numerical Result: Spam")
else:
    print("MultinomialNB Numerical Result: Not Spam")

# STEP 31 - MULTINOMIAL NB TF-IDF NEW MESSAGE
new_text_message = ["Congratulations! You have won a free cash prize. Call now to claim your reward 5000"]

# Convert new message into the same TF-IDF features
new_text_vector = text_vectorizer.transform(new_text_message)

# STEP 32 - MULTINOMIAL NB TF-IDF NEW PREDICTION
mnb_text_prediction = mnb_text_model.predict(new_text_vector)
mnb_text_probability = mnb_text_model.predict_proba(new_text_vector)
print("MultinomialNB TF-IDF Prediction:", mnb_text_prediction[0])
print("MultinomialNB TF-IDF Probability:", mnb_text_probability[0])
if mnb_text_prediction[0] == 1:
    print("MultinomialNB TF-IDF Result: Spam")
else:
    print("MultinomialNB TF-IDF Result: Not Spam")

# STEP 33 - MODEL COMPARISON GRAPH
models = ["GaussianNB","SVM","MNB Numerical","MNB TF-IDF"]
accuracy_values = [gnb_accuracy,svm_accuracy,mnb_accuracy,mnb_text_accuracy]
plt.bar(models, accuracy_values)
plt.title("Naive Bayes and SVM Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.show()