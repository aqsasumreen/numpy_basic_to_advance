# permutation = refers to the arrangement of elements.
# numpy random module provides two methods: i) shuffle() , ii) permutation()
from numpy import random
import numpy as np

a = np.array([3, 4, 5, 6, 7])
random.shuffle(a)
print(a)
# shuffle changes the original array

b = np.array([3, 4, 5, 6, 7])
print(random.permutation(b))  # no change on original array
print(b)
