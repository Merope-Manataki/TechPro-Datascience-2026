import numpy as np

A = [3, 1, -2, 0, 4, 5, 1, -1, 2]
A = np.array(A)
A = np.array(A).reshape(3,3)

A = np.linalg.inv(A)
print(A)









