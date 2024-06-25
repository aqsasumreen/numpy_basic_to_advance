# binomial distribution - tossing a coin results in either head or tail ,, only these two occurences
# so this is also called discrete dist based on binary output.
# parameters of this : n(number of trials) , p , size

from numpy import random
a = random.binomial(n= 10, p = 0.5, size= 5) #hr elem pr 10 dfa toss huwa
print(a)
#--> visualization

import matplotlib.pyplot as plt
import seaborn as sb
sb.distplot(random.binomial(n = 10 , p= 0.5 , size = 1000) , kde = False)
plt.show()
# kde = false means histogram in beautify form like separated columns

# difference between normal and binomial
sb.distplot(random.binomial(n = 10 , p= 0.5 , size = 1000) , label='binomial' , rug=True , hist= False)
plt.show()
sb.distplot(random.normal(loc = 50 , scale = 5 , size= 1000) , label='normal' , rug=True , hist= False)
plt.show()
