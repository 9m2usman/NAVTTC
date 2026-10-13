import numpy as np
arr = np.array([1,2,4,6])
np.save("my_array.npy",arr)
loaded = np.load("my_array.npy")
print(loaded)

# index select and condition
grid = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(grid[1,2]) # ans = 6
print(grid[grid>5]) #numbers at index greater than 5 will return

# 3x3 grid and print value at row 2 col 1 using index
grid2 = np.array([[4,3,2],[5,1,6],[7,8,9]])
print(grid2[2,1],grid2[grid2%2==0])

# arr of 5 num add 100 to every ele using broadcasting no loop
# multiply entire arrray by 3 then substract 1 from every element in two broadcast step
arr = np.array([2,3,4,5,7])
print(arr + 100, arr*3-1)


# type casting arthmetic op
import numpy as np
i = np.array([1.4,2.9,3.5])
print(i.astype(int))

j = np.array([4,5,6])
k = np.array([7,8,9])

print(i+j,i+k-j,i*j,k/i,i**2)

# flaot array woth dec cast using astype 
# 2 arrays of 4 num and print their sum dif prod an div

import numpy as np
i1 = np.array([3.4,5.9,7.5])
print(i1.astype(int))
i1 = i1.astype(int)
j1 = np.array([9,5,14])
print(i1+j1,j1-i1,i1*j1,j1/i1)

import numpy as np
m = np.array([1,4,9,16])
print(np.sqrt(m))
angle = np.array([15,30,45,60])
print(np.sin(angle))

# array of 5 perfect sq np.sqrt to get their root back
# arrray of angles and apply npsin to alll of them in a single line
m = np.array([1,4,9,16,25,36])
print(np.sqrt(m).astype(int))
angle = np.array([0,30,45,60,90])
print(f"{np.sin(angle)}\n,{np.cos(angle)}\n,{np.tan(angle)}")

import numpy as np
import os

arr = np.array([[1, 2, 4, 6],[4,6,7,9],[1,5,9,4]])

np.save("my_array.npy", arr)

print("File created at:")
print(os.path.abspath("my_array.npy"))

loaded = np.load("my_array.npy")
print(loaded)