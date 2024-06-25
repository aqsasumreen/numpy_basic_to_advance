import numpy as np

# Creating an ndarray
array = np.array([1, 2, 3, 4, 5])
print(array)


list_to_array = np.array([10, 20, 30])
print(list_to_array)


zeros_array = np.zeros((3, 3))
ones_array = np.ones((2, 2))
range_array = np.arange(0, 10, 2)  # Start at 0, end before 10, step by 2
print(zeros_array)
print(ones_array)
print(range_array)


random_array = np.random.rand(3, 3)
random_int_array = np.random.randint(0, 10, (3, 3))  # Random integers between 0 and 10
print(random_array)
print(random_int_array)


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
print(a - b)
print(a * b)
print(a / b)


array = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(array))
print(np.mean(array))
print(np.max(array))


import numpy as np
a = np.array([1,2,3,4,5])
# print(a[2])
# print(a[2] + a[1])

# Accessing the elements of 2-D , cosider it as rows and columns
b = np.array([[1,2,3],[4,5,6]])
print(b[0 , 1] , b[1,2]) # sec elem of 0 row. , third elem of sec row

# Accessing 3D array:
c = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[4,5,6]]])
print(c[0 ,0,2] , c[1,1,1]) # it consits of 2d arays, so 0 means first 2d,
#  next 0 means first row of first 2d , 2 means third elem


# slicing in 1D is similar to list
# 2D
import numpy as np
z = np.array([[1,2,3],[4,5,6]])
print(z[0 , 1:2])
print(z[0:2 , 0:3]) # 0,1 row ka 0-3


# We can pass list , tuple or any other dataType like object to
# an array And it will be converted to ndArray.

x = np.array([2,3,4,5])
print(x)
print(type(x))

zeros_array = np.zeros((3, 3))
ones_array = np.ones((2, 2))
range_array = np.arange(0, 10, 2)  # Start at 0, end before 10, step by 2
print(zeros_array)
print(ones_array)
print(range_array)



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

