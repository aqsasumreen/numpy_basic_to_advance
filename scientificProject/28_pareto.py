# params : a(shape), size

from numpy import random
pt = random.pareto(a= 2, size=(2,3))
print(pt)

# visualization
import matplotlib.pyplot as plt
import seaborn as sb
sb.distplot(random.pareto(a= 2, size=1999) , rug= True , hist= False)
plt.show()
