import numpy as np

# 1D numpy array
x = np.array([20, 40, 60])
print("Array x:", x)
print("Length of x:", len(x))
print("Type of x:", type(x))
print("Shape of x:", x.shape)
print("Data type of x:", x.dtype)

# Transpose of 1D array (no change for 1D)
x_t = x.T
print("Transpose of x:", x_t)
print("Shape of transpose:", x_t.shape)

# 2D numpy array with one row
y = np.array([[20, 50, 40]])
print("\nArray y:\n", y)
print("Shape of y:", y.shape)

# Transpose of y
y_t = y.T
print("Transpose of y:\n", y_t)

# Transpose of y transpose (back to original)
print("Transpose of y_t (back to y):\n", y_t.T)

# Zero vector with shape (3,1)
z = np.zeros((3, 1))
print("\nZero vector z:\n", z)

# Create a 1D array
one_d = np.array([5, 10, 15, 20])
print("\n1D array one_d:", one_d)
print("Shape of one_d:", one_d.shape)
print("Type of one_d:", type(one_d))

# Zero vector matching shape of one_d
one = np.zeros(one_d.shape)
print("Zero vector with shape of one_d:", one)
print("Length of zero vector:", len(one))

# Create a 2D numpy array B with shape (3, 2)
two_d = np.array([[1, 2], [3, 4], [5, 6]])
print("\n2D array two_d:\n", two_d)
print("Shape of two_d:", two_d.shape)
print("Type of two_d:", type(two_d))

# Zero matrix with same shape as two_d
zero = np.zeros(two_d.shape)
print("Zero matrix with shape of two_d:\n", zero)

# Transpose of two_d
two_d_t = two_d.T
print("Transpose of two_d:\n", two_d_t)
