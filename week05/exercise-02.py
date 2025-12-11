import numpy as np

heights_np = np.array([160,170,180,175])
weights_np = np.array([55,65,80,75])

covariance = np.cov(heights_np, weights_np)

print(covariance)
print(f"heights var: {heights_np.var()}")

