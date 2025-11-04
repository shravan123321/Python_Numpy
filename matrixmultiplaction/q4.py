import numpy as np

arr = np.array([[1,2,3,4]])      # shape (1, 4)
arr1 = np.expand_dims(arr, axis=1)  # expand dimension
arr11 = np.squeeze(arr1)            # remove single dimensions

print(arr1)
print(arr11)
 
#repeat the array elements 
arr3=np.repeat(arr,4)
print("repeat the array elements: ",arr3)