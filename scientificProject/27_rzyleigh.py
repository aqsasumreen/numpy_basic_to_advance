# rayleigh : used for signals processing in ML
# by default scale = 1.0
from numpy import random
a = random.rayleigh(scale = 2, size=(2,3))
print(a)
# visualization
import matplotlib.pyplot as plt
import seaborn as sb
sb.distplot(random.rayleigh(scale = 2, size=6000))
plt.show()

# on the same value of scale and df --> chi square and rayleigh shows same result
