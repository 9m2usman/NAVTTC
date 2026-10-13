import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = sns.load_dataset('tips') #.pits is already a stored dataset in library of sns
print(df.shape,"\n",df.head(),"\n", df.dtypes,"\n",df.tail())
print(df.describe()) # give mean std min 25% 50% 75% max

# how many records exist for each day of the week in the dataset(Mon,Tue,Wed,Thur,Fri,Sat,Sun)
print(df["day"].value_counts())
print(df.groupby("day")["day"].count())

# create a histogram showing how total_bill are distributed across the dataset dont forget to actually display it.
sns.histplot(
    data=df,
    x="total_bill",
    bins=10
)
plt.show()

# # find avg tial bill which dy has highest avg bill?
df = sns.load_dataset('tips')
print(df.groupby("day")["total_bill"].mean())
print()
print(df.groupby("day")["total_bill"].mean().idxmax(), df.groupby("day")["total_bill"].mean().max()) #idx max gives the day name that is as index

# scatter plot showing points total bill x tip y
df = sns.load_dataset('tips')
sns.scatterplot(
    df,
    x="total_bill",
    y="tip"
)
plt.show()


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')

# take total_bill tip nd size claculate how strongly they relate to each other then visualize ita s heatmap
corelation = df[["total_bill","tip","size"]].corr()
print(corelation)
sns.heatmap(
    corelation,
    annot = True
)
plt.show()
