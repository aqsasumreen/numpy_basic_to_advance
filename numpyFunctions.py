import numpy as np
# REVERSE NUMPY ARRAY
# The np.nan is a “constant representing a missing or undefined
# numerical value in a NumPy array”. It stands for “not a number”
# and has a float type. The np.nan is equivalent to NaN and NAN.


# How to ignore all numpy warnings(not recommended)

# import warnings
# warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)


myarr = np.array([1, 0, np.nan, 3])

print(myarr)

arr1 = np.array([[[1,2,3],[4,5,6]],
                [[7,8,9],[10,11,12]]])
res = arr1[::-1]
# print(res)
arr2 = np.array([[1,2,3],[4,5,6]])
rest = arr2[::-1]
print(rest)
rest = np.flip(arr2)
print(rest)
# A 3X3 WITH VALUES RANGING FROM 0-9
x =np.arange(0,9). reshape(3,3)
print(x)
# # FIND INDICES OF NON-ZERO ELEMENTS
# print(np.nonzero(arr1))
# 3X3X3 with random values
x = np.random.random((3,3,3))
print(x)
y = np.random.random((10,10))
print(y)
x = np.ones((5,5))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")
x[1:-1,1:-1] = 0
print(x)

# HOW TO FIND THE MEMORY SIZE OF NUMPY ARRAY:
print("size of array", arr3.size)
print("size of array element in bytes", arr3.itemsize)
print("total memory size", arr3.size*arr3.itemsize)
arr7 = np.array([2,2,9.3,3])
print("size of array", arr7.size)
print("size of array element in bytes", arr7.itemsize)
print("total memory size", arr7.size*arr7.itemsize)
arr8 = np.zeros((10))
print(arr8.size)
# Create a null vector of size 10 but the fifth value which is 1
vector= np.zeros((10))
vector[4]=1
print(vector)
# 7. Create a vector with values ranging from 10 to 49
vector1 =np.arange(10,49)
# print(vector1)
# 16. How to add a border (filled with 0's) around an existing array?
vector2= np.zeros((5,5))
print("Original array:")
print(vector2)
print("Boreder filled with zeros:")
vector2[1:-1,1:-1] = 1
# print(vector2)

# Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
matrix = np.zeros([5,5])
for i in range(1,5):
    matrix[i ,i-1] = i

# print(matrix)

# Create a 8x8 matrix and fill it with a checkerboard pattern
matrix2 = np.zeros([8,8])
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            matrix2[i,j] = 1

# print(matrix2)

# Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
array = np.arange(1,337).reshape(6,7,8)
# FIND THE INDEX OF 100th
index = np.where(array==100)
# print(index)

# The numpy.tile() function is used to construct an array by repeating
# a given array a certain number of times in a specified order.
#  The order of repetition can be controlled using the 'reps' parameter.

# Create a checkerboard 8x8 matrix using the tile function
checkboard = np.tile([[1,0], [0,1]] , (4,4))
print(checkboard)


# Normalize a 5x5 random matrix
# solution:
# Normalizing a matrix means scaling the values in the matrix so they
# They all fall within a specific range. One common way to normalize a
# matrix is to use the min-max normalization method, which scales
# the values in the matrix so that they range between 0 and 1

matrix3 = np.random.rand(5,5)
min_value = np.min(matrix3)
max_value = np.max(matrix3)
normalize_matrix = (matrix3-min_value)/(max_value-min_value)
# print("Normalize_matrix", normalize_matrix)


# Define the custom dtype
color_dtype = np.dtype([('R', np.uint8), ('G', np.uint8), ('B', np.uint8), ('A', np.uint8)])
# Create an array using the custom dtype
colors = np.array([(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255)], dtype=color_dtype)
# Print the array
# print(colors)


# Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix4 = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [10,11,12],
                   [13,14,15]])

# print(matrix4.shape)
matrix5 = np.array([[1,2,3],
                   [4,5,6],
                   [13,14,15]])

# print(matrix4 @ matrix5)

# array5 = np.array([0.5 , 3.5 ,1.6])
# rounded_array= np.round(array5 ,decimals =0 , away_from_zero=True)
# print(rounded_array)

# How to find common values between two arrays
match1 = np.array([2,3,4,5,8])
match2 = np.array([7,8,9,10,11])
set1= set(match1)
set2= set(match2)
intersection = set1.intersection(set2)
# only for 1d arrays
commomon_values = np.array(list(intersection))
# print(commomon_values)


# How to get the dates of yesterday, today and tomorrow
from datetime import datetime,  timedelta
# Get today's date
today = datetime.now()

# Get yesterday's date
yesterday = today - timedelta(days=1)

# Get tomorrow's date
tomorrow = today + timedelta(days=7)

# Print the dates
# print("Yesterday: ", yesterday.strftime("%Y-%m-%d"))
# print("Today: ", today.strftime("%Y-%m-%d"))
# print("Tomorrow: ", tomorrow.strftime("%Y-%m-%d"))

import calendar

# Get the number of days in July 2016
num_days = calendar.monthrange(2016, 7)[1]
# print(num_days)

# Extract the integer part of a random array of positive numbers
# using 4 different methods

import random
import math
# Create a random array of positive numbers
arr = [random.randint(1, 10) for i in range(10)]
# Extract the integer part of each number using `math.floor()`
int_arr = [math.floor(num) for num in arr]
# Print the original array and the integer array
# print("Original array:", arr)
# print("Integer array:", int_arr)


# Create a random array of positive numbers
arr2 = [random.randint(1, 10) for i in range(10)]
# Extract the integer part of each number using `math.floor()`
int_arr2 = [int(num) for num in arr2]
# Print the original array and the integer array
# print("Original array:", arr2)
# print("Integer array:", int_arr2)

# Create a random array of positive numbers
arr3 = [random.randint(1, 10) for i in range(10)]
# Extract the integer part of each number using `math.floor()`
int_arr3 = [num//1 for num in arr3]
# Print the original array and the integer array
# print("Original array:", arr3)
# print("Integer array:", int_arr3)

