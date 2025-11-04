#inverse the matrix 
import numpy as np

# correct inverse example
arr = np.eye(5)   # 3x3 identity matrix
print("Matrix:\n", arr)

arr_inv = np.linalg.inv(arr)
print("Inverse:\n", arr_inv)
