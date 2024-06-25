# random.normal() method: continuous distribution, loc(highest value or mean),
# scale(flat , standard deviation) , size
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sb
a = random.normal(size=(2,3))
print(a)

b = random.normal(loc=1 , scale=2 , size=(2,3))
print(b)

sb.distplot(random.normal(size=1000) ,rug=True, hist=False)
plt.show()

