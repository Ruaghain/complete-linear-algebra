import numpy as np

# Create two random-integer vectors (R4)
n = 4
v1 = np.round(20 * np.random.randn(n, 1))
v2 = np.round(20 * np.random.randn(n, 1))
print(v1)
print(v2)

# Compute the lengths of the individual vectors, and magnitude of their dot product
# np.sqrt(v1.dot(v1))
v1_magnitude = np.linalg.norm(v1)
print(v1_magnitude)
v2_magnitude = np.linalg.norm(v2)
print(v2_magnitude)
dpm = np.abs(np.sum(v1.dot(v2.transpose())))
print("dot product magnitude", v2_magnitude)

# normalize the vectors (create unit vectors along the same direction)
uv1 = v1 / v1_magnitude
print(uv1)
uv2 = v2 / v2_magnitude
print(uv2)

# Sanity check - the following should be equal to one.
v1u_magnitude = np.linalg.norm(uv1)
print(v1u_magnitude)
v2u_magnitude = np.linalg.norm(uv2)
print(v2u_magnitude)

# Compute the magnitude of that dot product
dpum = np.abs(np.sum(uv1.dot(uv2.transpose())))
print(dpum)

