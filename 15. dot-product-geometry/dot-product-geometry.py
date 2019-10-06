import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Two vectors
v1 = np.array([2, 4, -3])
v2 = np.array([0, -3, -3])

# Compute the angle (radians) between the two vectors.
ang = np.degrees(np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))))
print(ang)

# draw them
fig = plt.figure()
# ax = fig.gca(projection="polar")
ax = Axes3D(fig)
ax.plot([0, v1[0]], [0, v1[1]], [0, v1[2]], 'b')
ax.plot([0, v2[0]], [0, v2[1]], [0, v2[2]], 'r')

plt.axis((-6, 6, -6, 6))
plt.title('Angle between vectors: %s degrees.' %ang)
plt.show()
