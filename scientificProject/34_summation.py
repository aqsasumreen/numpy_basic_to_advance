# addition works n twom operators , but sum works on n numbers
import numpy as np
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([6, 7, 8, 9, 10])
a3 = np.sum([a1, a2]) # np.add(a1, a2)
# print(a3)

# we want sum of each array sepaarately
a4 = np.sum([a1, a2], axis=1)
# print(a4)

# --> Cummulative sum : means partially adding their elem in an array
a5 = np.cumsum([a1, a2])
# print(a5)

# ------------------------------35# Product ---------------------------------
a6 = np.prod([a1, a2])
# print(a6)

a7 = np.prod(a1)
# print(a7)

a8 = np.prod([a1, a2], axis=1)
# print(a8)

a9 = np.cumprod([a1, a2])
# print(a9)

# ---------------------------36# difference---------------------------------
# A discrete difference means subtracting two successive elements.
a10  = np.diff(a1)
# 2-1 , 3-2, 4-3, 5-4
print(a10)

a11 = np.diff([a1, a2])
print(a11)