# person    covid(y/n)    flu(y/n)     fever(y/n)
# 1           y               n           y
# 2           n               y           y
# 3           y               y           y
# 4           n               n           n 
# 5           y               n           y                 
# 6           n               n           y       
# 7           y               n           y   
# 8           y               n           n   
# 9           n               y           y
# 10          n               y           n

# formula : prob(y/x1+x2+x3+....+xn) = prob(x1/y),prob(x2/y),......prob(xn/y) ,   P(COVID∩Flu ∣ Fever) ,  P(COVID,Flu∣Fever)=P(COVID∣Fever)×P(Flu∣Fever)
# here we ave just 3 things in which one amongst them is based on other two and two features that is yes and no. y and no will be x and y
# first find prior probability of those two featues
#  prob(fever = y) = 7/10,  P(Fever=Y)=107​=0.7
#  prob(fever = n) = 3/10,  P(Fever=N)=103​=0.3   
#  conditional probabiltiy ==>    y      n
#        covid with fvr covid    4/7    2/3       
#        covid with flu  flu     3/7    2/3


# 2. When Fever = YES
# Take only these 7 people:
# Person	COVID	Flu	Fever
# 1	          Y 	N	Y
# 2           N	    Y   Y
# 3	          Y  	Y	Y
# 5	          Y 	N	Y
# 6	          N 	N	Y
# 7        	  Y	    N	Y
# 9	          N	    Y	Y

# P(COVID=Y∣Fever=Y)=7 4​=0.57
# P(COVID=N∣Fever=Y)=73=0.429
# P(Flu=Y∣Fever=Y)=73​=0.429
# P(Flu=N∣Fever=Y)=74​=0.571

# P(COVID,Flu∣Fever)
# P(COVID,Flu∣Fever)=P(COVID∣Fever)×P(Flu∣Fever) 

# COVID = YES, Flu = YES, Fever = YES
# 4/7 * 3/7 = 0.245

# COVID = YES, Flu = NO, Fever = YES
# 3/7 * 3/7 = 0.184

# COVID = YES, Flu = NO, Fever = YES
#  4/7 * 4/7 = 0.327

# COVID = NO, Flu = NO, Fever = YES
# 3/7 * 4/7 = 0.245

# actual
# | COVID | Flu | Actual people | Actual probability |
# | :---: | :-: | ------------: | -----------------: |
# |   Y   |  Y  |      Person 3 |    1/7 = **0.143** |
# |   Y   |  N  | Persons 1,5,7 |    3/7 = **0.429** |
# |   N   |  Y  |   Persons 2,9 |    2/7 = **0.286** |
# |   N   |  N  |      Person 6 |    1/7 = **0.143** |

# naive byes
# | COVID | Flu | **Actual** | **Naive Bayes** |
# | :---: | :-: | ---------: | --------------: |
# |   Y   |  Y  |      0.143 |           0.245 |
# |   Y   |  N  |      0.429 |           0.327 |
# |   N   |  Y  |      0.286 |           0.184 |
# |   N   |  N  |      0.143 |           0.245 |




# # model fitting and coding
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import GaussianNB
# from sklearn.metrics import accuracy_score, confusion_matrix

# df = pd.read_csv("6_naive_byes/students_week5.csv")
# x = df.drop(columns= ["student_id", "final_score", "result", "performance"]) # input features
# y = df["result"]  # output feature
# x_train, x_test, y_train, y_test = train_test_split (x, y, test_size= 0.2, random_state = 42, stratify = y)

# model = GaussianNB() # no scaling needed
# model.fit(x_train, y_train)
# pred = model.predict(x_test)
# print("Accuracy:", accuracy_score(y_test, pred))
# print(confusion_matrix(y_test, pred))

# new_student = x_test.iloc[[1]] # one student from the test set
# print ("Pass Probability:", model.predict_proba(new_student)[0][0].round(2))





# for counting of multiple num datas 
# Yes. For **Naive Bayes**, if you have **two items depending on a third item**, such as:
# * COVID
# * Flu
# * Fever
# and we want to understand:
# > **Probability of COVID and Flu together, given Fever**
# we write:
# P(COVID \cap Flu \mid Fever)
# But Naive Bayes makes the important assumption that **COVID and Flu are conditionally independent given Fever**.
# So:
# {P(COVID,Flu\mid Fever) = P(COVID\Fever) * P(Flu\Fever)
# ### Simple YES/NO example
# Suppose we have this data:
# | Fever | COVID | Flu | Count |
# | ----- | ----- | --- | ----: |
# | Yes   | Yes   | Yes |    30 |
# | Yes   | Yes   | No  |    20 |
# | Yes   | No    | Yes |    25 |
# | Yes   | No    | No  |    25 |
# | No    | Yes   | Yes |     5 |
# | No    | Yes   | No  |    10 |
# | No    | No    | Yes |    10 |
# | No    | No    | No  |    75 |

# Let's focus only on people with **Fever = Yes**.
# Total:
# 30+20+25+25=100

# ### 1. Probability of COVID given Fever
# COVID = Yes and Fever = Yes:
# 30+20=50

# Therefore:
# P(COVID=Yes\mid Fever=Yes) ={50}{100}=0.5
# ### 2. Probability of Flu given Fever
# Flu = Yes and Fever = Yes:
# 30+25=55

# Therefore:
# P(Flu=Yes Fever=Yes)={55}{100}=0.55

# ### 3. Probability of COVID AND Flu given Fever
# Naive Bayes assumes conditional independence:
# P(COVID,Flu\mid Fever)=P(COVID\ Fever) * P(Flu\ Fever)

# Therefore:
# =0.5*0.55 = {0.275}

# So the Naive Bayes calculation gives **27.5%**.
# ## Now with YES/NO combinations
# This is probably the table you're looking for:
# | COVID | Flu | Fever | Formula                                         |
# | ----- | --- | ----- | ----------------------------------------------- |
# | Yes   | Yes | Yes   | \(P(Covid=Y\|Fever=Y)\times P(Flu=Y\|Fever=Y)\) |
# | Yes   | No  | Yes   | \(P(Covid=Y\|Fever=Y)\times P(Flu=N\|Fever=Y)\) |
# | No    | Yes | Yes   | \(P(Covid=N\|Fever=Y)\times P(Flu=Y\|Fever=Y)\) |
# | No    | No  | Yes   | \(P(Covid=N\|Fever=Y)\times P(Flu=N\|Fever=Y)\) |

# Using our numbers:
# P(Covid=Y\mid Fever=Y)=0.50
# P(Covid=N\mid Fever=Y)=0.50
# P(Flu=Y\mid Fever=Y)=0.55
# P(Flu=N\mid Fever=Y)=0.45

# So:
# | COVID | Flu |                   Probability |
# | ----- | --- | ----------------------------: |
# | Yes   | Yes | \(0.50\times0.55=\) **0.275** |
# | Yes   | No  | \(0.50\times0.45=\) **0.225** |
# | No    | Yes | \(0.50\times0.55=\) **0.275** |
# | No    | No  | \(0.50\times0.45=\) **0.225** |
# Notice: 0.275+0.225+0.275+0.225=1

# ### The reasoning
# Think of Fever as the condition/context
#                  Fever = YES
#                      │
#           ┌──────────┴──────────┐
#           ↓                     ↓
#        COVID                  Flu
#        YES/NO                YES/NO
#           │                     │
#           └──────────┬──────────┘
#                      ↓
#              Multiply probabilities

# The key Naive Bayes idea is:
# Given Fever, we treat COVID and Flu as independent for the calculation.
# So instead of trying to directly calculate:
# P(COVID and(intersection) Flu\ Fever)
# we calculate two simpler probabilities and multiply them:
# {P(COVID\Fever) * P(Flu\Fever)}
# This is exactly where the **"Naive"** assumption comes from.


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("./Datasets/students_week5.csv")
x = df.drop(columns= ["student_id", "final_score", "result", "performance"]) # input features
y = df["result"]  # output feature
x_train, x_test, y_train, y_test = train_test_split (x, y, test_size= 0.2, random_state = 42, stratify = y)

models = {'Logistic Regressoin': LogisticRegression(max_iter=1000),
          'SVM (rbf) ':SVC(kernel='rbf'),
          'SVM (linear)':SVC(kernel='linear'),
          'KNN (k=5)': KNeighborsClassifier(9),
          'Naive Bayes ': GaussianNB()}

for name, m in models.items():
    pipe = make_pipeline(StandardScaler(), m).fit(x_train,y_train)
    print(f'Model Name :{name:20s} accuracy = {pipe.score(x_test, y_test):.3f}')