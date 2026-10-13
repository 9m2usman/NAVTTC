#pandas and DataFrame = spreedsheet kind of data rows and cols
import pandas as pd
data = {
    "name" : ["Ali","Sarah","Ahmed","Hassan"],
    "marks" : [85,75,92,65]
}
df = pd.DataFrame(data)
print(df)

# task DataFrame creation for 4 students wit columns : name,city,score
# print the DataFrame and identify how any rows and columns it has.
std = {
    "name" : ["usman","ahmed","luqman","abdullah"],
    "city" : ["atd","nawanshehr","mandia","isb"],
    "scroe" : [24,35,56,75]
}

sdf = pd.DataFrame(std)
print(sdf,"\ntheir num of rows and cols",df.shape)

# # series : single labled col data e.g upper we have col name = name city and score accessing any one col is called series.
import pandas as pd
s = pd.Series([10,20,30,40], index=["a","b","c","d"])
print(s)

s2 = pd.Series([["usman","zeeshan","ali"],[20,30,40]], index = ["name","num"])
print(s2)

df = pd.DataFrame({"name":["ali","sara"],"score":[85,92]})
print(df["name"])

# create a series of 5 city with custom index label c1,c2,...
# DataFrame of your choice, extract one col and print its type using type
c = pd.Series(["multan","kar","isb","lhr","atd"], index=["c1","c2","c3","c4","c5"])
print(c)

df2 = pd.DataFrame({"name":["ali","sara"],"score":[85,92]})
print(df["name"],df["score"],type(df["name"]))

# operations and condition based response
import pandas as pd
df = pd.DataFrame({"name":["ali","sara","ahmed","noman","yasir"],"score":[85,92,50,60,80]})
print(df[df["score"]>=80])

# marks greater than 75
df2 = pd.DataFrame({"name":["ali","sara","ahmed","noman","yasir"],"score":[85,92,50,60,80]})
print(df2[df2["score"]>75])

# marks and name togather using double square brackets
print(df2[["name","score"]], "\n", df2[["name","score"]].values)

# # sorting of data through marks changing one col and all table change acc to it.
import pandas as pd
df = pd.DataFrame({"name":["ali","ahmed","usman"],"marks":[27,78,45]})
df["grade"] = df["marks"].apply( lambda x: "pass" if x>=45 else "fail")
print(df.sort_values("marks",ascending=True))

# new col to dataframe aply that lable rows high or low basd on value
df2 = pd.DataFrame({"name":["usman","ahmed","ali"],"values" : [54,34,67]})
df2["pos"] = df2["values"].apply(lambda x: "high" if x>54 else "low")
print(df2.value_counts())
# num of std who are pass 
print(df2[df2["pos"] == "high"]["name"].value_counts)

# # handling missing data
import pandas as pd
df = pd.DataFrame({"name":["usman",None,"ahmed"],"marks":[None,23,45]})
print(df.isnull)
print(df.fillna(0))

import pandas as pd
sales = pd.DataFrame({"name":["it","it","hr","it","hr"],"sales":[23,45,100,30,36]})
print(sales.groupby("name")["sales"].sum())

# catageroies and price col gorup by catageor to find avg_price of products of dataframe
# gourpby with.count to find how many record exist in eaach
products = pd.DataFrame({"cat":["mobile","tv","laptop","mobile","tv"],"price":[23,45,100,30,36]})
print(products.groupby("cat")["price"].mean())
print(products.groupby("cat")["cat"].count(),"\n",products.groupby("cat")["cat"].size())

# # joins = how = "inner/left/right"
import pandas as pd
a = pd.DataFrame({"id":[1,2,3],"name":["usman","sara","ali"]})
b = pd.DataFrame({"id" : [1,2,4],"marks":[85,92,4]})
print(pd.merge(a,b, on = "id", how = "inner" )) 

c = pd.DataFrame({"id":[1,2,3,4,5],"name":["usman","ali","ahemd","zoya","abdullah"]})
d = pd.DataFrame({"id":[1,2,6,7],"rollNum":[22704,227003,227011,227022]})
print(pd.merge(c,d, on = "id", how = "left"), pd.merge(c,d, on = "id", how = "inner"))
# concat will do later

# # pandas plottin visual not text
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({"dept":["it","hr","sale"],"revenue":[250,170,300]})
df.plot(x="dept",y="revenue",kind = "bar")
plt.show()

import pandas as pd
c = pd.DataFrame({"id":[1,2,3,4,5],"name":["usman","abdullah","ahemd","zoya","ali"]})
d = pd.DataFrame({"id":[1,2,6,7],"rollNum":[22704,227003,227011,227022]})
# print(pd.merge(c,d, on = "id", how = "left"), pd.merge(c,d, on = "id", how = "inner"))
print(pd.concat([c[["id","name"]],d[["id","rollNum"]]]).values)
print(pd.merge(c,d, on = "id", how = "left"))