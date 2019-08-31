import matplotlib.pyplot as plt
import numpy as np

v1 = np.array([3, -1])
l = -.3
v1m = v1 * l  # scalar-modulated

# plot them
plt.plot([0, v1[0]], [0, v1[1]], 'b', label='v_1')
plt.plot([0, v1m[0]], [0, v1m[1]], 'r:', label='\lambda v_1')

plt.axis('square')
plt.axis((-4, 4, -4, 4))
plt.grid()
plt.show()
