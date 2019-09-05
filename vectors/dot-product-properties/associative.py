import numpy as np

## Associative property

# create random vectors
n = 10
a = np.random.randn(n)
b = np.random.randn(n)
c = np.random.randn(n)

# the two results
res1 = np.dot(a, np.dot(b, c))
res2 = np.dot(np.dot(a, b), c)

# compare them
# print(res1)
# print(res2)
print([res1, res2])

### special cases where associative property works!
# 1) one vector is the zeros vector
# 2) a==b==c
