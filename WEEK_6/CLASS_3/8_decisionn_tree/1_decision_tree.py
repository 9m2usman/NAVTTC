# # Decision Tree
# # gini = 1 - sum(probability^2) the tree tries every feature and cut it and finds the cut that gives the lowest gini impurity (best split)
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier, export_text

# df = pd.read_csv("8_decisionn_tree/students_week5.csv")
# X = df.drop(columns=["student_id", "final_score","result","performance"])
# y = df["result"]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # no scaling need of trees.
# for depth in [3,5,None]:
#     tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
#     tree.fit(X_train, y_train)
#     print(f"max_depth={depth} Train accuracy: {tree.score(X_train, y_train):.3f}, Test accuracy: {tree.score(X_test, y_test):.3f}")

# # see the rules of the tree
# small = DecisionTreeClassifier(max_depth=1, random_state=42).fit(X_train, y_train)
# t_5 = DecisionTreeClassifier(max_depth=5, random_state=42).fit(X_train, y_train)
# print(export_text(small, feature_names=list(X.columns)))
# print(export_text(t_5, feature_names=list(X.columns)))



# # random forest = many trees, each tree sees a random subset of features and rows, then the final prediction is the majority vote of all trees (for classification) or average (for regression)
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier

# df = pd.read_csv("8_decisionn_tree/students_week5.csv")
# X = df.drop(columns=["student_id","final_score","result","performance"])
# y = df["result"]
# x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

# # 200 trees each train on random sample of rows + features
# forest = RandomForestClassifier(n_estimators=200, random_state=42)
# forest.fit(x_train,y_train)
# print(f'Random Forest Train accuracy: {forest.score(x_train,y_train):.3f}, \nRandom Forest Test accuracy: {forest.score(x_test,y_test):.3f}')

# # which features mattered most
# importance = pd.Series(forest.feature_importances_,index=X.columns)
# print(importance.sort_values(ascending=False).round(3))



# boosting = many trees, each tree sees all features and rows, but each tree focuses on the rows that were misclassified by the previous trees. The final prediction is the weighted vote of all trees (for classification) or weighted average (for regression)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

df = pd.read_csv("8_decisionn_tree/students_week5.csv")
X = df.drop(columns=["student_id","final_score","result","performance"])
y = df["result"]
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

# 200 trees each train on all rows + features, but each tree focuses on the rows that were misclassified by the previous trees
boost = GradientBoostingClassifier(n_estimators=200, random_state=42)
boost.fit(x_train,y_train)
print(f'Gradient Boosting Train accuracy: {boost.score(x_train,y_train):.3f}, \nGradient Boosting Test accuracy: {boost.score(x_test,y_test):.3f}')
