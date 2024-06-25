from numpy import random
a = random.chisquare(df= 2, size=(3,4))
print(a)
# visualization
import matplotlib.pyplot as plt
import seaborn as sb
sb.distplot(random.chisquare(df=2, size=(599)), rug=True, hist=False)
plt.show()