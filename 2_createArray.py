import numpy as np

x = np.array([2,3,4,5])
print(x)
print(type(x))

# We can pass list , tuple or any other dataType like object to
# an array And it will be converted to ndArray.a.
y = np.array((6,7,8,9))
print(y)
print(type(y))

# Dimensions in array - dimensions are level of depth in array
# 1#  0-D : each element in an array is a 0-dimensional
# . --> in [2,3,4] , each of elem is 0-d
# 2#  1-D : has  0-D arrays as its elements --> [2,3,4,5]
# 3#  3-D : has 1-D arrays as its elements:

z = np.array([[1,2,3],[4,5,6]])
print(z.ndim)

## 3-D : has 2-D arryas as its elements.
a = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[4,5,6]]])
print(a.ndim)

# 4-D
b = np.array([[[[1,2,3],[4,5,6]],
              [[7,8,9],[4,5,6]]],
              [[[1,2,3],[4,5,6]],
              [[7,8,9],[4,5,6]]]])

print(b.ndim)

# Create array with 5-D
c = np.array([1,2,3,4,5] , ndmin=5 )
print(c)
