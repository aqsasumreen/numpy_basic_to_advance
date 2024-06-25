# concate arrays with numpy
import numpy as np

a = np.array([2,3,4,5])
a1 = np.array([1,7,8,9])
a2 = np.concatenate([a,a1])
# print(a2)

#--> concat 2D along with rows(axis = 1)
b = np.array([[1, 2, 3], [4, 5, 6]])
b1 = np.array([[7, 8, 9], [9, 10, 11]])
b2 = np.concatenate([b,b1],axis = 1) #combines  row of first with the second , doesn`t work for 1D
# print(b2)

#--> stacking
c = np.array([2,3,4,5])
c1 = np.array([1,7,8,9])
c2 = np.stack([c,c1], axis=1) #plays on indexes, combines 0 of first with 0 of second,
# print(c2)
# print(c2.ndim) #2D

d = np.array([2,3,4,5])
d1 = np.array([1,7,8,9])
d2 = np.hstack([d,d1]) #simple combines both arrays as row wise,
print(d2)

e = np.array([2,3,4,5])  
e1 = np.array([1,7,8,9])
e2 = np.vstack( [e,e1]) #simple comnies both arrays as coulmn wise, & 2D
print(e2)
print(e2.ndim)

f = np.array([2,3,4,5])
f1 = np.array([1,7,8,9])
f2 = np.dstack( [f,f1]) #simple comnies both arrays as coulmn wise, , & 3D
print(f2)
print(f2.ndim)

