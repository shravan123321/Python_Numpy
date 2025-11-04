# diffrent between as array and asany array
import numpy as np

mat=np.matrix([[1,2,3],[4,5,6]])

a1=np.asarray(mat)
a2=np.asanyarray(mat)

print("original array: ",mat)
print("asarray: ",a1)
print("asanyarray: ",a2)

print("type asarray: ",type(a1))
print("type asanyarray:",type(a2))