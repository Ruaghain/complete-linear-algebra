import numpy as np

# Test whether the dot product sign is invariant to the scalar multiplication

# Generate two vectors
# Transpose the two arrays to make them column vectors (not strictly necessary)
v1 = np.transpose(np.array([-3, 4, 5]))
v2 = np.transpose(np.array([3, 6, -3]))

print(v1)
print(v2)

# Generate two scalars
s1 = -2
s2 = 3

# Compute the dot product between vectors
dot_product = np.dot(v1, v2)
print("dot product between v1 and v2 is: ", dot_product)
# The dot product for these two vectors is 0, which means that they meet at a right angle.

# fig = plt.figure()
# ax = fig.gca()
# ax.plot([0, v1[0]], [0, v1[1]], [0, v1[2]], 'b')
# ax.plot([0, v2[0]], [0, v2[1]], [0, v2[2]], 'r')
# plt.axis((-10, 10, -10, 10))
# plt.show()

# Compute the dot product between the scaled vectors
scaled_dot_product = np.dot(s1 * v1, s2 * v2)

print("Scaled dot product:", scaled_dot_product)
