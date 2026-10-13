# svm find the widest "street/line" b/w classes. only closest descides the support vectors- decides where it goes.
# maximise margin = 2/||w||

# hyperplane : the sperating line/plane(orange)
# margin : gap b/w the dashed lines
# support vector : circle points touching the margin
# c(parameters) : small c = wider margin, allow mistakes

# kernel=(linear) : straight boundary(margin) works when casses can be split by line 85.5 accurace
# kernel=(rbf) :  curved boundary default. maps data to higher dimension so curved boundary is possible 90.5 acuracy
# c and gamma :

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,r2_score

df = pd.read_csv("E:/navttcPython/Datasets/students_week5.csv")
x = df.drop(columns=['student_id','final_score','result','performance'])
y = df['result']

# svm need scaler features
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42,stratify=y)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

for krnl in ['linear','poly','rbf','sigmoid']:
    model = SVC(kernel=krnl, C=1.0)
    model.fit(x_train,y_train)
    acc = accuracy_score(y_test,model.predict(x_test))
    r2 = r2_score(y_test,model.predict(x_test))
    print(f"SVM   kernel : {krnl}, Accuracy : {acc:.3f}, r2_score : {r2}")



# knn : k neariest neighnor
# k num of neighbor
# distancec = distance formula = sqrt( (x1-y1)**2 + (x2-y2)**2 + .... )
# scaling first then picked the best around k = 9
# small k = underfit (noisy),  large k = overfit (too_smooth)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("E:/navttcPython/Datasets/students_week5.csv")
x = df.drop(columns=['student_id','final_score','result','performance'])
y = df['result']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

# without scaling first
raw = KNeighborsClassifier(n_neighbors=5).fit(x_train,y_train)
print(f"kNN without scaling : {accuracy_score(y_test,raw.predict(x_test))}")

# now with scaling
scaler = StandardScaler()
x_train_s,x_test_s = scaler.fit_transform(x_train), scaler.transform(x_test)

for k in [1,3,5,7,9,15,25]: #find the best k
    knn = KNeighborsClassifier(n_neighbors=k).fit(x_train_s,y_train)
    acc = accuracy_score(y_test,knn.predict(x_test_s))
    print(f"k = {k:>2} : accuracy = {acc:.3f}")