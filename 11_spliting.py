# splitting of 1D
import numpy as np
a = np.array([1, 2, 3, 4])
a1 = np.array_split(a, 3)
print(a1)
# we can`t use in this form so for this
print(a1[0])
print(a1[1])

b = np.array([[1, 2],[3,4], [6, 7], [8,9]])
b1 = np.array_split(b, 3)
print(b1)

# split 2D along with rows
c = np.array([[1, 2],[3,4], [6, 7], [8,9]])
c1 = np.array_split(c, 2 , axis=1)
print(c1)

# alternative is hsplit()
d = np.array([[1, 2],[3,4], [6, 7], [8,9]])
d1 = np.hsplit(d, 2 )
print(d1)


