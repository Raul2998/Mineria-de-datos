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
print ('La suma de las Victorias del Equipo Azul es:', data['blueWins'].sum(), 
       '\nLa suma de las Victorias del Equipo Red es:', data['redWins'].sum())
print('-------------------------------------------------------------------------------\n')

sel_cols = ['blueWardsPlaced', 'redWardsPlaced', 'blueTotalGold','redTotalGoldredTotalGold']
##cols = data[sel_cols]

# Buscamos el maximo valor de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
print('El maximo valor de Wards del equipo azul colocados es:', data['blueWardsPlaced'].max(),
      '\nEl maximo valor de Wards del Equipo Rojo colocados es:', data['redWardsPlaced'].max(), 
      '\nEl maximo valor del Total de Oro ganado del Equipo Azul es:', data['blueTotalGold'].max(), 
      '\nEl maximo valor del Total de Oro ganado del Equipo Red es:', data['redTotalGold'].max())
print('-------------------------------------------------------------------------------\n')

# Bsucamos el minimo valor de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
print('El minimo valor de Wards del equipo azul colocados es:', data['blueWardsPlaced'].min(),
      '\nEl minimo valor de Wards del Equipo Rojo colocados es:', data['redWardsPlaced'].min(), 
      '\nEl minimo valor del Total de Oro ganado del Equipo Azul es:', data['blueTotalGold'].min(), 
      '\nEl minimo valor del Total de Oro ganado del Equipo Red es:', data['redTotalGold'].min())
print('-------------------------------------------------------------------------------\n')

# Calculamos el conteo de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
print('El conteo de Wards del equipo azul colocados es:', data['blueWardsPlaced'].count(),
      '\nEl conteo de Wards del Equipo Rojo colocados es:', data['redWardsPlaced'].count(), 
      '\nEl conteo del Total de Oro ganado del Equipo Azul es:', data['blueTotalGold'].count(), 
      '\nEl conteo del Total de Oro ganado del Equipo Red es:', data['redTotalGold'].count())
print('-------------------------------------------------------------------------------\n')

# Calculamos la moda de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
print('El valor de la moda de Wards del equipo azul colocados es:', data['blueWardsPlaced'].mode(),
      '\nEl valor de la moda de Wards del Equipo Rojo colocados es:', data['redWardsPlaced'].mode(), 
      '\nEl valor de la moda del Total de Oro ganado del Equipo Azul es:', data['blueTotalGold'].mode(), 
      '\nEl valor de la moda del Total de Oro ganado del Equipo Red es:', data['redTotalGold'].mode())
print('-------------------------------------------------------------------------------\n')

# Calculamos la media de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
print('La media de Wards del equipo azul colocados es:', data['blueWardsPlaced'].mean(),
      '\nLa media de Wards del Equipo Rojo colocados es:', data['redWardsPlaced'].mean(), 
      '\nLa media del Total de Oro ganado del Equipo Azul es:', data['blueTotalGold'].mean(), 
      '\nLa media del Total de Oro ganado del Equipo Red es:', data['redTotalGold'].mean())
print('-------------------------------------------------------------------------------\n')

# Calculamos la varianza de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
print('La varianza de Wards del equipo azul colocados es:', data['blueWardsPlaced'].var(),
      '\nLa varianza de Wards del Equipo Rojo colocados es:', data['redWardsPlaced'].var(), 
      '\nLa varianza del Total de Oro ganado del Equipo Azul es:', data['blueTotalGold'].var(), 
      '\nLa varianza del Total de Oro ganado del Equipo Red es:', data['redTotalGold'].var())
print('-------------------------------------------------------------------------------\n')

# Calculamos la desviacion estandar de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
print('La desviacion estandar de Wards del equipo azul colocados es:', data['blueWardsPlaced'].std(),
      '\nLa desviacion estandar de Wards del Equipo Rojo colocados es:', data['redWardsPlaced'].std(), 
      '\nLa desviacion estandar del Total de Oro ganado del Equipo Azul es:', data['blueTotalGold'].std(), 
      '\nLa desviacion estandar del Total de Oro ganado del Equipo Red es:', data['redTotalGold'].std())
print('-------------------------------------------------------------------------------\n')

# Calculamos la asimetria de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
print('La asimetria de Wards del equipo azul colocados es:', data['blueWardsPlaced'].skew(),
      '\nLa asimetria de Wards del Equipo Rojo colocados es:', data['redWardsPlaced'].skew(), 
      '\nLa asimetria del Total de Oro ganado del Equipo Azul es:', data['blueTotalGold'].skew(), 
      '\nLa asimetria del Total de Oro ganado del Equipo Red es:', data['redTotalGold'].skew())
print('-------------------------------------------------------------------------------\n')