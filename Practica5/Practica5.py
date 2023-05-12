#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 5: LINEAR MODELS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import statsmodels.api as sm

data = pd.read_csv('C:/Users/raulh/OneDrive/Documentos/Mineria-de-datos/lol_dataframe2.csv')

# Creando eje X y eje Y
x = data['blueKills']
y = data['blueTotalGold']

# Separando las variables en training y testing
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.7, test_size = 0.3, random_state = 100)

# Visualizamos el dataset train
print(x_train, y_train)

# Agregamos una constante para obtener la interseccion
X_train_sm = sm.add_constant(x_train)

# Ajustamos la regresion lineal usando'OLS'
lr = sm.OLS(y_train, X_train_sm).fit()

# Impresion de los parametros
print(lr.params)

# Performing a summary to list out all the different parameters of the regression line fitted
print(lr.summary())

# Visualizamos la regresion lineal
plt.scatter(x_train, y_train)
plt.plot(x_train,  1.368e+04  + 457.7481*x_train, 'r')
plt.show()