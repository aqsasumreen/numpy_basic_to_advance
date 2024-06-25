# sin(), cos() and tan() that take values in radians and produce the corresponding
# sin, cos and tan values.
import numpy as np
a = np.sin(np.pi/2)
print(a)

# for array
a1 =np.sin([np.pi/2, np.pi/4, np.pi/6])
print(a1)

# convert degree to radians
a2 = np.deg2rad([90,180,270,360]) #rad is pi/180
# print(a2)

# convert  radians to degrees
a3 = np.rad2deg([np.pi/5, np.pi/7, np.pi/9, 3*np.pi/11]) #deg is 180/pi
# print(a3)

# numpy provides arcsin(), arccos(), and arctan() for finding angles
# a4 = np.arctan(np.pi/5)
a5 = np.arcsin(1)
print(a4)
print(a5)

arr = np.array([1, -1, 0.1])
a6 = np.arctan(arr)
print(a6)

# Finding hypotenues using pythagoras theorem in NumPy.
b= 4
prep = 8
x = np.hypot(b,prep)
print(x)



