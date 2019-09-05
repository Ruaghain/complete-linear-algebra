import numpy as np

ROWS = 4
COLUMNS = 6

A = np.random.randint(1, 20, size=(ROWS, COLUMNS))
B = np.random.randint(1, 20, size=(ROWS, COLUMNS))

print(A)
print(B)

column_product = np.zeros(COLUMNS)
for i in range(0, COLUMNS):
    column_product[i] = np.dot(A[:, i], B[:, i])

print("Dot product result is:", column_product)
