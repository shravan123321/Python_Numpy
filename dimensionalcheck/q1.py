# define the dimensional cheking numpy 
import numpy as np
# zero dimensional 
arr1=np.zeros([5])
print("zero dimensional: ",arr1)

# one dimensional 
arr2=np.ones([2])
print("one dimensional: ",arr2)

'''
# define the two dimensional 
# jaise hum two dimensional karege to error aata hai qki numpy two dimension exit nahi karta hai 
arr3=np.twos(4)
print("two dimensional :",arr3)
'''

# so solved the problem in this numpy
arr3=np.zeros((3,5)) # two dimensional array
print("two dimensional: ",arr3)
# ager hum aushaka ager three dimensional banana chahta hu to me numpy me syntax aish ho jata hai
arr4=np.zeros((1,3,5)) # three dimensional array
print("three dimensional array; ",arr4)

# how to check the dimensional in the array so picture visulized the down side 

# one dimensional ([])
# tow dimensional ([[]])
# three dimensional ([[[]]])
# four dimensional ([[[[]]]]) 

# just incresse the ([])