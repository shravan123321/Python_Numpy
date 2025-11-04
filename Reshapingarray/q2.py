# define the numpy array and then access the particular array elements 
import numpy as np
 
arr=np.random.randint(0,10,(5,5))
print("elements array: ",arr)

# access the array elements first 3 row
arr1=arr[0:3]
# array elements access row form me :
print("access the array elements: ",arr1)

# array elements access the row and colon form me 
arr2=arr[0:4,[1,3]]
print("accessing the elements particular: ",arr2)