#define the reshaping array 
import numpy as np

arr=np.random.randint(0,10,size=(3,4))
print("array elements: ",arr)

# Change the array digram 
# 1 idea
arr1=arr.reshape(2,6)
print("change the array digram(row,colon): ",arr1)
# 2 idea
arr2=arr.reshape(4,3)
print("change the array digram(row,colon): ",arr2)
#3 idea
arr3=arr.reshape(1,12)
print("change the array digram(row,colon)",arr3)
# there are multiple idea generated array digram but total elements 12 hona chahiye ager 12 se jada elements dal dijiye ga to error aata hai 
#Example:--
# arr4=arr.reshape(2,5)
# print(arr4)

#Ager hum array ke original shape karna chahte hai to meghe bash ke used karna prega
arr5=arr.reshape(-1,2).base
print("array original shape: ",arr5)