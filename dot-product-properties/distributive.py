import numpy as np

## Distributive property

# create random vectors

n = 10
a = np.random.randn(n)
b = np.random.randn(n)
c = np.random.randn(n)

# the two results
res1 = np.dot(a, (b + c))
res2 = np.dot(a, b) + np.dot(a, c)

# compare them
# print([res1, res2])
print(res1)
print(res2)
