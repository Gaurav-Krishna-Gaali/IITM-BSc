import numpy as np
V = [0, 1, 2, 3, 4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]

size = len(V)
Amat = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    Amat.append(row.copy())


for (i, j) in E:
    Amat[i][j] = 1
print(Amat)


AMat = np.zeros(shape=(size, size))

for (i, j) in E:
    AMat[i, j] = 1
print(AMat)
