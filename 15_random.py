from numpy import random

a = random.randint(100)
print(a)

b = random.rand(100)  #generate random float
print(b)
# generate array

c = random.randint(100 , size=(3,5))  #2D array with 5elements in each
print(c)

d = random.rand(3,5)
print(d)

# you can also generate random number from given array
e = random.choice([3,5,7,9,11])
print(e)
# form 2D array:

f = random.choice([1,3,5,7,9,11,13] , size=(3,5))
print(f)
