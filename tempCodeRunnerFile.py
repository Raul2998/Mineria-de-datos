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

# Buscamos el conteo de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
print('El conteo de Wards del equipo azul colocados es:', data['blueWardsPlaced'].count(axis=1),
      '\nEl conteo de Wards del Equipo Rojo colocados es:', data['redWardsPlaced'].count(), 
      '\nEl conteo del Total de Oro ganado del Equipo Azul es:', data['blueTotalGold'].count(), 
      '\nEl conteo del Total de Oro ganado del Equipo Red es:', data['redTotalGold'].count())
print('-------------------------------------------------------------------------------\n')