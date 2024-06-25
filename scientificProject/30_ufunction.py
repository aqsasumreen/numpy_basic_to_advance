# universal functions are the built in functions of numpy
import numpy as np

# without uFunction
x = [1,3,5,7]
y = [2,4,6,8]
z = []
for i,j in zip(x,y):
    z.append(i+j)
print(z)

# with uFunction
z = np.add(x, y)
print(z)

# 31-build own uFunction-------------------------
def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd[[1,2,3,4],[5,6,7,8]])

print(type(np.add))

# function is ok,,but still giving error


