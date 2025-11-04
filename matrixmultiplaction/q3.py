# define the array and then expand the array
import numpy as np

#array elements particular colon form me 
array_data = np.expand_dims([1, 2, 3, 4], axis=0)
print(array_data)
print("Shape of array:", array_data.shape)

# array elements particular row form me
array_data=np.expand_dims([1,2,3,4],axis=1)
print(array_data)
print("shape of the array: ", array_data.shape)