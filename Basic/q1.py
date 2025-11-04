" time check the numpy array and python list"
import numpy as np
import timeit
execution_time = timeit.timeit("np.arange(1,9)", setup="import numpy as np", number=10000)
print(f"Execution time: {execution_time}")
