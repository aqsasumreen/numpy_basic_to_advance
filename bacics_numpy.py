import numpy as np
# import  urllib
# this library working with urls
# arr1 = np.array([2,3,4])
# print(arr1.ndim)
# arr2 = np.array([[1,2,3],
#                  [4,5,6],
#                 [7,8,9]])
# print(type(arr2))
# print(arr2.dtype)
# print(arr2.shape)
# print(arr2.ndim)
# print(arr2.size)

arr3 = np.array([[[1, 2, 3], [4, 5, 6]],
                [[7, 8, 9], [10, 11, 12]]])
arr4 = np.array([[[11, 12, 13], [14, 15, 16]],
                [[7, 8, 9], [10, 11, 12]]])
con = np.concatenate((arr3, arr4), axis=1)
print(con)
print(np.max(arr3))
print(np.min(arr3))
print(np.median(arr3))
print(np.mean(arr3))
print(np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0))
print(type(arr3))
print(arr3.dtype)
print(arr3.shape)
print(arr3.ndim)
print(arr3.size)
print(arr3)

#--> MATRIX MULTIPLICATION
# By default multiplication

print(np.matmul(arr3 , arr1))
# 2
print(arr3 @ arr1)

# ----------------Fetching array elements--------
print(arr3[1,1,2])
# phli list 0 dosri 1 ;dosri pe phli 0 dosri 1 then again usme..
print(arr3[1:,0:1,:2])
# in exact number selection then number of ranges redues , but in range it maintains the number
print(arr3[1:,0:1,:2].shape)
print(arr3[1,1,:3])
print(arr3[1,1])
print(arr3[:2,1])
print(arr3[: ,0:1])
print(arr3[: ,::1])
#1 ki difference se sara aye ga...
# ----------------------------CREATING NUMPY ARRAYS----------------------
arr4=np.zeros((3,2))
print(arr4)
#
arr5=np.ones((2,2,3))
print(arr5)
# identity matrix
arr6=np.eye((2))
print(arr6)
# rand function generates values from 0 to 1
# randn generrates from -2 to 2 ,,also generates from probability distribution--
arr7 = np.random.rand(5)
print(arr7)
arr8 = np.random.randn(2,3)
print(arr8)
# CREATING ARRAYS WITH FIXED VALUES
arr9 = np.full([2,3],42)
print(arr9)
arr10 = np.arange(10, 50, 3)
print(arr10)
print(arr10.shape)
arr11 = np.linspace(10, 50, 15)
print(arr11)

