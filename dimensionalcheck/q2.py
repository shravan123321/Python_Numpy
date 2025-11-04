# random number 

# define the randon number print in numpy
import numpy as np
arr=np.random.random_sample()
# so in this number user not the input automaticaly output compiler so
print("random number output: ",arr) 

print("Ager user ke random  output number chahiye to used the numpy libeary ")
arr1=np.random.rand(5)
print("Minimum Five number outpu: ",arr1)

# this methods used and then two dimensional array 
arr2=np.random.randint(1.5,size=(3,4))
print("two dimensional random: ",arr2)
print("Check the array dimensional: ",arr2.ndim)
print("Check the array size: ",arr2.size)
