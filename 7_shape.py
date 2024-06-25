# shape is basically number of elements present in each dimension
import numpy as np
x = np.array([2,3,4,5])
print(x.shape)
# each square brackets represents the dimension
z = np.array([[1,2,3],[4,5,6]])
print(z.ndim)
print(z.shape) #phli square bracket me 2 elements ,un dono me 3 elements--> 2,3

a = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[4,5,6]]])
print(a.ndim)
print(a.shape) # phli me do ele , dosri me 2 , teesri me 3 -->2,2,3


b = np.array([[[[1,2,3],[4,5,6]],
              [[7,8,9],[4,5,6]]],
              [[[1,2,3],[4,5,6]],
              [[7,8,9],[4,5,6]]]])

print(b.ndim)
print(b.shape) # 2,2,2,3

c = np.array([1,2,3,4,5] , ndmin=5 )
print(c.shape) #1,1,1,1,5