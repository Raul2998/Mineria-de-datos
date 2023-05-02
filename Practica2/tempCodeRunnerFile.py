#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 2: DESCRIPTIVE STATISTICS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/raulh/OneDrive/Documentos/Tareas/Mineria de datos/lol_dataframe2.csv')
sel_cols = ['blueWardsPlaced', 'redWardsPlaced', 'blueTotalGold','redTotalGold']
wins = ['blueWins', 'redWins']
a = data[sel_cols]
b = data[wins]

# Definimos nuestro funcion para calcular la media
def media(data):
    mean = data.mean()
    return mean

#Definimos nuestra funcion para calcular la suma 
def suma(data):
    sum = data.sum()
    return sum

# Visualizamos nuestro dataframe por sus categorias\
data.info()
print('-------------------------------------------------------------------------------\n')

# Calculamos la suma individual de las columnas blueWins y redWins
blueWins, redWins = b.apply(suma)