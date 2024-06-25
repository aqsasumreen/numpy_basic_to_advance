import numpy as np

a = np.array([2, 4, 5, 7])
a1 = np.where(a == 5)
# print(a1)

b = np.array([2, 4, 5, 7])
b1 = np.where(b % 2 != 0)
# print(b1)
# search sorted() performs
c = np.array([2, 4, 5, 7])
c1 = np.searchsorted(c, 6)
# print(c1)

d = np.array([2, 4, 5, 7])
d1 = np.searchsorted(d, [1, 3, 8])
# print(d1)


#--------------------------13-sorting---------------------------

e = np.array([2, 6, 1, 8, 7])
print(np.sort(e))

f = np.array(['cherry', 'banana', 'apple'])
print(np.sort(f))

#---------------------------14-filtering ------------------------
g = np.array([3,4,5,6,8,10,2])
g_empty = g>6
g_new = g[g_empty]
print(g_new)
print(g_empty)

# Alternative  way of applying for loop and write if condition inside that..
