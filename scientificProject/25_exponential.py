# Exponential distribution: We analyze the data and expect
# whether the next event will fail or succeed.
# params: scale (inverse of rate (lambda)), size
from numpy import random
a = random.exponential(scale= 2, size=(2,3))
# print(a)

# visualization
import matplotlib.pyplot as plt
import seaborn as sb
sb.distplot(random.exponential(size = 1000), rug=True, hist= False)
plt.show()

# Poisson: How many times an event has occurred.
# Exponential: The time between occurrences of an event.
