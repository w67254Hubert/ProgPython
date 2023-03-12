import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])
newarr=arr.reshape(3,3,3)
print(newarr)
print(newarr.ndim)