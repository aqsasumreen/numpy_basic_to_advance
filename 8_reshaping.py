# reshaping is changing the shape of an array ny adding or removing the element..
# reshape from 1D to 2D
import numpy as np
a = np.array([1,2,3,4,5,6,7,8])
a1 = a.reshape(4,2)
print(a1.shape)
print(a1.ndim)#2

# reshape 1d to 3d
b = np.array([1,2,3,4,5,6,7,8])
b1 = b.reshape(2,2,2)
print(b1.shape) #2,2,2
print(b1.ndim)

# return copy or view
c = np.array([1,2,3,4,5,6,7,8])
print(c.reshape(2,4).base) #return the original ,means this is view

# you are only allowed to have one unknown dimension
d = np.array([1,2,3,4,5,6,7,8])
d1 = d.reshape(2,2,-1)
print(d1)

#flattening the array by converting into 1d
e = np.array([[1,2,3], [4,5,6]])
e1 = e.reshape(-1)
print(e1)

# alot of functions for changing the shape of an array like flatten , ravel and also
# rearranging the elem rot90 , flip , flipir , flipud..







