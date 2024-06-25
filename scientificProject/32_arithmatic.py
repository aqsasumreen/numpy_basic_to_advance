import numpy as np
a = np.array([10, 20, 30, 40, 50])
b = np.array([6, 7, 8, 9, 10])
a1 = np.add(a, b)
print(a1)
b1 = np.subtract(a, b)
print(b1)
c1 = np.multiply(a, b)
print(c1)
d1 = np.divide(a, b)
print(d1)
e = np.power(a, b)
print(e)
a2 = np.mod(a, b)
print(a2)
a3 = np.remainder(a, b)
print(a3)
a4 = np.divmod(a, b) # give both qoutient and remainder
print(a4)


