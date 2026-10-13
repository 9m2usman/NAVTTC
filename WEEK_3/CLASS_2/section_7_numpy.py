# numpy and creating arrays..
import numpy as np
arr = np.array([1,4,5,9,3])
print(arr);

# zeros = matrix of 0 with .zeros(rows,cols)
zeros = np.zeros((2,3))
print(zeros)

# random numbers .rand.randint(startpoint, endExcludedPoint, how_many_num_in_row)
rand = np.random.randint(1,10,5) # 5 will give 5 num in a row
print(rand)

# numpy creation five fav num and print it.
arr2 = np.array([2,5,7,8,9])
print(arr2)

# np.one of 3x3 and array of 4 integers between 1 and 100

ones = np.ones((3,3)) 
print(ones)

rand2 = np.random.randint(1,100,4)
print(rand2)


# shpae = dimension rows and colm of array
# dtype datatype tells 
# size = total num of elements.  ndim= num of dimensions

a = np.array([[1,4,6,8],[2,5,7,9]])
print(a.shape,a.dtype,a.size,a.ndim)

# 2d array of shape 3,4 using any num and then print shape size and ndim
a1 = np.array([[1,4,6,8],[2,5,7,9],[5,8,2,6]])
print(a.shape,a.size,a.ndim)

a2=np.array([1.0,1,2.0])
print(a2.dtype,a1.dtype)

# reshape = change from [row,col] to [col,row]
# min max argmax=index of max value and argmin = index of min value

b = np.array([2,5,7,1,8,9])
print(b.reshape(6,1),b.max(),b.min(),b.argmax(),b.argmin())

# create 1d array of 6 num reshape it into 2,3 array then print the reshape result.
b2 = np.array([2,5,7,1,8,9])
print(b2, b2.reshape(6,1))

# find min max of that array
print(b2.min(),"at index : ",b2.argmin(),"\n",b2.max(),"at index : ",b2.argmax())

b2d = np.array([[2,5,1,8,3,1],[1,2,5,7,9,6]])
print(b2d.reshape(4,3))

# min max argmin argmax of random array of 8 nums between 1-100
randarr = np.random.randint(1,100,8)
print(f"your random array : {randarr}")
print(f"{randarr.min()} min val at index : {randarr.argmin()}\n{randarr.max()} max value at index : {randarr.argmax()} ")

# # copy=making duplicate append=add at end and insert= add at ur desire position,
# copy & view: copy make copy of orignal change one wont change other but in .view make copy change one change other too
# .vew.base = an array which is copied but in .copy.base = none
c = np.array([1,2,3])
c_copy = c.copy()
c_copy[0] = 99
print(c,c_copy)

d = np.array([1,2,3])
print(np.append(d,[4,7]))
print(np.insert(d,1,100)) #np.insert(array_name,position/index,value)

# crete array make copy midify copy tand confirm the original array is unaffected.
cd = np.array([1,2,3])
cd_copy = c.copy()
cd_copy[0] = 99
print(cd,cd_copy)

# append 3 new num to array then insert at pos 2 of the origianal array
print(np.append(cd,[8,4,7]))
print(cd)
cd = np.append(cd,[3,8,5])
print(cd,np.insert(cd,3,20))

# sort(array) delete(array,positon/index) combine and split = equal parts required, aplit_array = equal parts not required
import numpy as np
e = np.array([5,3,8,1])
print(np.sort(e),np.delete(e,0))

f1,f2=np.array([2,5,6,8]),np.array([3,5,7,8])
print(np.concatenate((f1,f2)))
print(np.array_split(np.arange(1,7),3)) #np.arange here tell the range that is 1 to 6 for 3 arrays that is splitted into 0-2 for every array 

a1,a2=np.array([4,6,3,7]),np.array([8,3,4,1])
a1_a2_comb = np.concatenate((a1,a2))


# unsort array of 6 num and sort it then del at index 2
e1 = np.array([5,3,5,8,1])
print(np.sort(e),np.delete(e,2))

# concatenate two arrays of your choice then split the combined result into 2 equal parts
f4,f3=np.array([2,5,6,8]),np.array([3,5,7,8])
comb = np.concatenate((f3,f4))
comb = np.sort(comb)
print(comb,np.array_split(comb,2))


