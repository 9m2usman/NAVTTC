import pandas as pd
df = pd.DataFrame({
    "name":["ali","ahemd","ali"],
    "marks":[85,92,85]
})
print(df.duplicated())
print(df.drop_duplicates())

# create duplicates and remove 
df = pd.DataFrame({
    "name":["ali","ahemd","ahmed"],
    "marks":[85,92,92]
})
print(df.duplicated())
print(df.drop_duplicates())

# Outlier : out of range Lower Boundry - Upper Boundry
#upper boundary = Q3+1.5*IQR
#lower boundary = Q1-1.5*IQR
#Q3 = middle value of last half of 8 num array
#Q1 = middle vlaue of fist half of 8 num array
#IQR = Q3 - Q1 but array should be arranged in asscending order




# data transformation:
import pandas as pd
import numpy as np
prices = pd.Series([100,2000,40000,500000])
# apply transformation convert pkr to usd
usd_price = prices *1.1
print(usd_price)

log_price = np.log(prices)
print(log_price)

# task

# encoding categorical variables
import pandas as pd
from sklearn.preprocessing import LabelEncoder
sizes = ["Small","Medium","Large","Medium"] #if u repeat value alreaday assigned will be given to its new value
color = ["blue","red","green","blue","alpha","red","REd","rEd"] 
le = LabelEncoder()
print(le.fit_transform(sizes), le.fit_transform(color)) #fit_transform first alphabet assign like in dict then assign them numbers


# feature scaling...
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

val = np.array([[10],[20],[30],[40],[50]])
ss = StandardScaler() # use this ss in print or simply like minMaxScaler() direct call upto u
print(ss.fit_transform(val).flatten()) #findout how much current num is scatter/away from our mean value z=(cur_val - mean)/(std_dev)
print(MinMaxScaler().fit_transform(val).flatten()) #where is this val b/w min and max : z = (current_val - min_val)/(max_val-min_val)


# task
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

val = np.array([[100],[250],[300],[400],[1000]])
print(StandardScaler().fit_transform(val).flatten()) #findout how much current num is scatter/away from our mean value
print(MinMaxScaler().fit_transform(val).flatten()) #find where is value lies b/w min and max
