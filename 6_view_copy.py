# diff between view and copy is that  , any change in copied array
# doesn`t affect original
# array  but in view both affected
import numpy as np

a = np.array([1, 2, 3, 4])
a1 = a.copy()
a1[0] = 90
print(a)  # no change
print(a1)

b = np.array([1, 2, 3, 4])
b1 = b.view()
# b1[0] = 90
b[0] = 90
print(b)  # no change
print(b1)

