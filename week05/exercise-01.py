import numpy as np
import scipy

data_lst = [ 4,6,7,6,3,1,6,4]
data_np = np.array(data_lst)

print(f"Average: { data_np.mean() }")
print(f"Median: { np.median(data_np) }")
print(f"Mode: {scipy.stats.mode(data_np).mode}")
print(f"Range: {data_np.min() - data_np.max()}")
print(f"Var: {data_np.var()}")
print(f"STD: {data_np.std()}")






