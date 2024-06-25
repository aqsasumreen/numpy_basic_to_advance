import numpy as np

# i for integer
# b for boolean
# u for unsigned integer
# f for float
# c for complex float
# m for timedelta
# M for dateTime
# O for object
# S for string
# U for unicode string(languages code)
# V for memory

a = np.array([2, 3, 4, 5])
print(a.dtype)
# creating array with defined dtype
b = np.array([4, 5, 6, 7], dtype='S')
print(b.dtype)  #S for  string
print(b)

c = np.array(['apple', 'banana'])
print(c.dtype) #U6

# an array with dataType of 4byte int
d = np.array([2,3,4,6], dtype='i4')
print(d.dtype) #32
# casting error
e = np.array([a,b,4,6], dtype='i4')
print(e.dtype)

# The astype() function creates a copy of the array, and allows you to specify the data type
# as a parameter. The data type can be specified using a string, like 'f' for float,
# 'i' for integer etc. or you can use the data type directly like float for float and int for integer.
f = np.array([2, 3, 4, 5])
g = f.astype(bool)
print(g)
print(g.dtype)