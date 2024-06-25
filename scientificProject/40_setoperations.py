# in numpy we use unique() for set, works on only 1d
import numpy as np
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)

a1 = np.array([2,4,6,8, 10,13])
a2 = np.array([1,3,5,7,10,13])
a3 = np.union1d(a1, a2)
print(a3)
a4 = np.intersect1d(a1, a2)
print(a4)
a5 = np.setdiff1d(a1, a2)
print(a5)

# Finding Symmetric Difference:
# To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
a6 = np.setxor1d(a1, a2)
print(a6) # other than unique
