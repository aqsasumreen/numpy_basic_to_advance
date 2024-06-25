import numpy as np
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
# print(x)
# reduce function give 1D
arr = np.array([3, 6, 9])

x1 = np.lcm.reduce(arr)
# print(x1)

arr1 = np.arange(1,11)
x2 = np.lcm.reduce(arr1)
# print(x2)
#
# --------------------->38#GCD---------------------
# gcd is greates common devisor
num1 = 4
num2 = 6
y = np.gcd(num1, num2)
print(y)

# gcd for array also used reduce  function
arr= np.array([8,12,20, 36])
y2 =np.gcd.reduce(arr) #also divisible by 2 but highest is 4
print(y2)


