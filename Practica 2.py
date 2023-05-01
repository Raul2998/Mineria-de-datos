#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 2: DESCRIPTIVE STATISTICS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/raulh/OneDrive/Documentos/Tareas/Mineria de datos/lol_dataframe2.csv')
# Visualizamos nuestro dataframe por sus categorias\
data.info()
print('-------------------------------------------------------------------------------\n')

# Calculamos la suma individual de las columnas blueWins y redWins
print ('La suma de las Victorias del Equipo Azul es:', data['blueWins'].sum(), '\nLa suma de las Victorias del Equipo Red es:', data['redWins'].sum())
print('-------------------------------------------------------------------------------\n')

# Buscamos la moda de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
print('El valor de la moda de Wards del equipo azul colocados es:', data['blueWardsPlaced'].mode(),'\nEl valor de la moda de Wards del Equipo Rojo colocados es:', 
      data['redWardsPlaced'].mode(), '\nEl valor de la moda del Total de Oro ganado del Equipo Azul es:', data['blueTotalGold'].mode(), 
      '\nEl valor de la moda del Total de Oro ganado del Equipo Red es:', data['redTotalGold'].mode())
print('-------------------------------------------------------------------------------\n')

# Buscamos el maximo valor de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
print('El maximo valor de Wards del equipo azul colocados es:', data['blueWardsPlaced'].max(),'\nEl maximo valor de Wards del Equipo Rojo colocados es:', 
      data['redWardsPlaced'].max(), '\nEl maximo valor del Total de Oro ganado del Equipo Azul es:', data['blueTotalGold'].max(), 
      '\nEl maximo valor del Total de Oro ganado del Equipo Red es:', data['redTotalGold'].max())
print('-------------------------------------------------------------------------------\n')

# Buscamos el minimo valor de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
print('El minimo valor de Wards del equipo azul colocados es:', data['blueWardsPlaced'].min(),'\nEl minimo valor de Wards del Equipo Rojo colocados es:', 
      data['redWardsPlaced'].min(), '\nEl minimo valor del Total de Oro ganado del Equipo Azul es:', data['blueTotalGold'].min(), 
      '\nEl minimo valor del Total de Oro ganado del Equipo Red es:', data['redTotalGold'].min())
print('-------------------------------------------------------------------------------\n')

# Creamos una funcion donde sacamos la media de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
def media(data):
    mean = data.mean()
    return mean

sel_cols = ['blueWardsPlaced', 'redWardsPlaced', 'blueTotalGold', 'redTotalGold']

b = data[sel_cols]

blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold = b.apply(media)

print('La media de Wards del equipo azul colocados es:', blueWardsPlaced,'\nLa media de Wards del Equipo Rojo colocados es:', redWardsPlaced,
      '\nLa media del Total de Oro ganado del Equipo Azul es:', blueTotalGold, '\nLa media del Total de Oro ganado del Equipo Red es:', redTotalGold )
print('-------------------------------------------------------------------------------\n')

# Creamos dos funciones, una para sacar la Varianza y otra para la Desviacion estandar de las columnas: gameDuration, queueId y seasonId
def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    variance = [ (x - mean) **2 for x in series]
    variance = sum(variance) / len(variance)
    return variance

def calc_stdev(series):
    variance = calc_variance(series)
    return variance ** (1/2)

gD_var, qI_var, sI_var = b.apply(calc_variance)
gD_stdev, qI_stdev, sI_stdev = b.apply(calc_stdev)

print('La varianza de gameDuration, queueId, seasonId es:', gD_var, qI_var, sI_var)
print('La desviacion estandar de gameDuration, queueId, seasonId es:', gD_stdev, qI_stdev, sI_stdev)