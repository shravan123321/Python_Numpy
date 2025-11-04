#define the linear equation in the equation samikaran 
# 7x+4y-2z=10
# 2x-2y+3z=0
# -2x+3y+2z=2

# solved the equation smikaran 

import numpy as np
# first step in set the equation 
a=np.array([[7,4,-2],[2,-2,3],[-2,3,2]])
print(a)
# then put the value for another array variable
b=np.array([10,0,2])
print(b)

# then finally given the value and then so solved the equations 
equations=np.linalg.solve(a,b)
# convert float to integer
equations = equations.astype(int)
print(f"x = {equations[0]}, y = {equations[1]}, z = {equations[2]}")
