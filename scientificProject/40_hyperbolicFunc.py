# numpy provides sinh(), cosh(),tanh() function
import numpy as np
a = np.sinh(9)
a = np.sinh(np.pi/2)
print(a)
arr = np.array([np.pi/7, 3*np.pi/8, np.pi/9])
a1 = np.tanh(arr)
print(a1)

# finding angels
a2 = np.arctanh(1.0) # only for arcsinh(), arccosh(), arctanh gives infinity
print(a2)
#
a3 = np.arcsinh([1.0, -1])
print(a3)
a4 = np.arccosh([1.0, -1*np.pi/2])
print(a4)

