# Zipf: Used to check which word/term appears most frequently in a dataset.
# param: a (distribution parameter), size
from numpy import random
pt = random.zipf(a= 2, size= (2,3))
print(pt)

# visualization
import matplotlib.pyplot as plt
import seaborn as sb
sb.distplot(pt[pt<10])
plt.show()