# Uniform Distribution -- only made for probability
# parameters -- a(lower bound - 0.0) ,b(upper bound - 1.0) , size
from numpy import random
a = random.uniform(size=(2,3))
print(a)


# visualization
import matplotlib.pyplot as plt
import seaborn as sb
sb.distplot(random.uniform(size=1000), rug=True , hist=False)
plt.show()

