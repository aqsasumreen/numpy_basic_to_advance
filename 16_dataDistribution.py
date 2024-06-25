# data distribution is the list of all possible values and how often each value occur.
# Random distribution : probability function
# p=1
from numpy import random
a = random.choice([1,2,3,4] , p=[0.2, 0.3, 0.4, 0.1] , size=(100))
print(a)

b= random.choice([1,2,3,4] , p=[0.2, 0.3, 0.4, 0.1] , size=(3 , 5))
print(b)

