# define the array and then transpor the array 
import numpy as np
arr1=np.random.randint(1,2,(3,3))
arr2=np.random.randint(0,10,(3,3))

# transpor the array 

print("original array: ",arr1, '\n'"transport the array: ",arr1.T)
print("original array: ",arr2, '\n'"transport the array: ",arr2.T)