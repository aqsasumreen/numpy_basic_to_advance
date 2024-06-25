# logistic and normal distributions are identical diff can be measured
# on the base of mean ,, logistic has more value of probability/ possibility
# than normal
# logistic describes growth it is basically imp in regression and neural network..
from numpy import random
a = random.logistic(loc  = 1 , scale = 2 , size = (2,3))
print(a)


# visualization
import matplotlib.pyplot as plt
import seaborn as sb

sb.distplot(random.logistic(size=1000) ,rug=True, hist=False)
plt.show()