# one way to iterate with simple for loop, for 2D and 3D use nested loops
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
for i in a:
    for j in i:
        print(j)

# other way to iterate in numpy
b = np.array([[1,2,3],[4,5,6]])
for i in np.nditer(b):
    print(i)

c = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[4,5,6]]])
for j in np.nditer(c):
    print(j)

# iterate in diff step sizes
d = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[4,5,6]]])
for k in np.nditer(d[: , ::2 ,::2 ]):
    print(k)