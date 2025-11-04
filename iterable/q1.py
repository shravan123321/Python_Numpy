# Basic iterable used the numpy 
import numpy as geek
num=int(input("enter the number: "))
iterable=(i for i in range(num))
number=geek.fromiter(iterable,int)
print(number)