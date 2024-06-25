# Multinomial distribution: It is a generalization of the binomial distribution.
# In binomial, we consider scenarios/sequences such as the blood type of a population.
# Multinomial describes the outcome of a scenario.
# parameters: n (number of trials or outcomes, e.g., how many times a dice is rolled),
# pvals (list of probabilities for each outcome, e.g., the possible outcomes of a dice roll from 1 to 6),
# size (shape of the returned array).

# Multinomial will not produce single value, they will produce one value for each
# possibility / pvals
# no need of visualization, because value kept on changing, e.g: difference value
# each dice roll

from numpy import random
a = random.multinomial(n= 6 , pvals = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(a)
