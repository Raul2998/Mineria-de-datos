#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 5: LINEAR MODELS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import statsmodels.api as sm

data = pd.read_csv('C:/Users/raulh/OneDrive/Documentos/Mineria-de-datos/lol_dataframe2.csv')
# Creating X and y
x = data['blueKills']
y = data['blueTotalGold']

# Splitting the varaibles as training and testing
x_train, X_test, y_train, y_test = train_test_split(x, y, train_size = 0.7, test_size = 0.3, random_state = 100)

# Take a look at the train dataset
print(x_train,y_train)

# Adding a constant to get an intercept
X_train_sm = sm.add_constant(x_train)

# Fitting the resgression line using 'OLS'
lr = sm.OLS(y_train, X_train_sm).fit()

# Printing the parameters
print(lr.params)

# Performing a summary to list out all the different parameters of the regression line fitted
print(lr.summary())

# Visualizing the regression line
plt.scatter(x_train, y_train)
plt.plot(x_train,  1.368e+04  + 457.7481*x_train, 'r')
plt.show()