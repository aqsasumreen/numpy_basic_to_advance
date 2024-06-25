# poisson Distribution - discrete distribution ,,aik events predict krta hy given data se
# supp din me 2x rice khaye tou 3sri khany ki probability kitni hoi
# parameters : lam(no.of occurrences or rate) , size
# generate a random  1*10 for occurrence 2


from numpy import random
a = random.poisson(lam = 2 , size =10)
# print(a)

# visualization
import matplotlib.pyplot as plt
import seaborn as sb
sb.distplot(random.poisson(lam = 2 , size =1000) , kde = False )
# plt.show()

# diff between normal and poisson
sb.distplot(random.normal(loc = 50 , scale = 5 , size= 1000) , label = 'normal', rug=True , hist= False)
plt.show()
sb.distplot(random.poisson(lam = 2 , size =1000) ,label = 'poisson', rug=True , hist= False)
plt.show()



