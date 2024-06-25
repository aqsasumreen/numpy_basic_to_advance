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