# there are 5 ways of rounding decimals:: truncate , fix , rounding,
# floor , ceil

import numpy as np
# -->Truncation
# Remove the decimals, and return the float number closest to zero.
arr = np.trunc([-3.1666, 3.6667])
print(arr) # [-3. 3.]

arr1 = np.fix([-3.1666, 3.6667])
print(arr1) # [-3. 3.]

# --> Rounding
# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
arr2 = np.around(3.1666, 2)
print(arr2) # [3.17]

# -->Floor
# The floor() function rounds off decimal to nearest lower integer.
arr = np.floor([-3.1666, 3.6667])
print(arr) # [-4. , 3. ]

# --> Ceil
# The ceil() function rounds off decimal to nearest upper integer.
arr = np.ceil([-3.1666, 3.6667])
print(arr) # [-3. , 4. ]