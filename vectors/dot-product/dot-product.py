import numpy as np

v1 = np.array([1, 2, 3, 4, 5])
v2 = np.array([0, -4, -3, 6, 5])

# method 1
dp = sum(np.multiply(v1, v2))
print("Using sum: ", dp)

# method 2
dp = np.dot(v1, v2)
print("Using dot: ", dp)

# method 3
dp = np.matmul(v1, v2)
print("Using matmul: ", dp)

# method 4
dp = 0  # initialize
# loop over elements
for i in range(0, len(v1)):
    # multiply corresponding element and sum
    dp = dp + v1[i] * v2[i]

print("Using iterate: ", dp)
