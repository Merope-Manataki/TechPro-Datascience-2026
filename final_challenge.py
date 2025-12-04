import numpy as np
w = [[3, 1, -2], [0, 4, 5], [1, -1, 2]]
w = np.array(w)
print(w)

w_rev = np.linalg.det(w)
print(w_rev)