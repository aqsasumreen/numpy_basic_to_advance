import  numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# random and uniform data
np.random.seed() #model br br generate ho tou wo same rhy,,
# 2 vars ko relate kr sky , agr phli br me 2,5,7 aya tou next me b aye
heights = np.random.normal(160, 10, 100)
weights =  0.6 + heights + np.random.normal(0, 5, 100)
# print(heights)


# spliting the data for training and testing
# ---> its a thumb rule that we train 80% data and test 20% data
X = heights.reshape(-1, 1)  #coulmn vector
Y = weights
X_train , X_test , Y_train, Y_test = train_test_split(X, Y, test_size = 0.2 , random_state =42)

# create and train the linear regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# Make prrediction using the trained model
Y_pred = model.predict(X_test) # 20%

# Visualize
plt.scatter(X_test, Y_test , color = 'blue' , label = 'Actual data')
plt.plot(X_test, Y_pred , color = 'red' , label = 'Regression line')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('linear regression -- Height VS Weight')
plt.legend()
plt.show()

# regression line shows k kitna model pr data fit hy









