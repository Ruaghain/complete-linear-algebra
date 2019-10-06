import numpy as np

# equivalence of algebraic and geometric dot product formulas
# two vectors

v1 = np.array([2, 4, -3])
v2 = np.array([0, -3, -3])

ang = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

# algebraic
dot_product_algebraically = np.dot(v1, v2)

# geometric
dot_product_geometrically = np.linalg.norm(v1) * np.linalg.norm(v2) * np.cos(ang)

# print dot product to command
print("Algebraically", dot_product_algebraically)
print("Geometrically", dot_product_geometrically)
