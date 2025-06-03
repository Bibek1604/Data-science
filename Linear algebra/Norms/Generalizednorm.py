##generalized norm
import numpy as np

gn=np.array([25, 2, 5])
p = 3  # You can change this value to any positive integer
generalized_norm = np.sum(np.abs(gn) ** p) ** (1 / p)
print(generalized_norm)
# generalized norm
# answer is 15.588457268119896 because it is the p-norm of the array, which is the sum of the absolute values raised to the power of p, then taking the p-th root.
# In this case, the p-norm is calculated as follows:
# 1. Take the absolute values of the elements in the array: |25|, |2|, |5| = 25, 2, 5
# 2. Raise each absolute value to the power of p: 25^3, 2^3, 5^3 = 15625, 8, 125
# 3. Sum the results: 15625 + 8 + 125 = 15758
 