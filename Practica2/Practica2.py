#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 2: DESCRIPTIVE STATISTICS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/raulh/OneDrive/Documentos/Tareas/Mineria de datos/lol_dataframe2.csv')
sel_cols = ['blueWardsPlaced', 'redWardsPlaced', 'blueTotalGold','redTotalGold']
wards = ['blueWardsPlaced', 'redWardsPlaced']
gold = ['blueTotalGold','redTotalGold']
minions = ['blueTotalMinionsKilled','redTotalMinionsKilled']
wins = ['blueWins', 'redWins']
a = data[sel_cols]
b = data[wins]

# Definimos nuestra funcion para calcular la suma 
def suma(data):
    sum = data.sum()
    return sum

# Definimos nuestra funcion para calcular la media
def mean(data):
    mean = data.mean()
    return mean

# Definimos nuestra funcion para calcular el minimo valor
def min(data):
    min = data.min()
    return min

# Definimos nuestr funcion para calcular el minimo valor
def max(data):
    max = data.max()
    return max

# Definimos nuestra funcion para calcular el conteo
def count(data):
    count = data.count()
    return count

# Definimos nuestra funcion para calcular la moda
def mode(data):
    mode = data.mode()
    return mode

# Definimos nuestra funcion para calcular la varianza
def var(data):
    var = data.var()
    return var

# Definimos nuestra funcion para calcular la desviacion estandar
def std(data):
    std = data.std()
    return std

# Definimos nuestra funcion para calcular la asimetria
def skew(data):
    skew = data.skew()
    return skew

# Visualizamos nuestro dataframe por sus categorias\
data.info()
print('-------------------------------------------------------------------------------\n')

# Calculamos la suma individual de las columnas blueWins y redWins
blueWins, redWins = b.apply(suma)
print ('La suma de las Victorias del Equipo Azul es:', blueWins, 
       '\nLa suma de las Victorias del Equipo Red es:', redWins)
print('-------------------------------------------------------------------------------\n')

# Buscamos el maximo valor de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
blueWardsPlacedMax, redWardsPlacedMax, blueTotalGoldMax, redTotalGoldMax = a.apply(max)
print('El maximo valor de Wards del equipo azul colocados es:', blueWardsPlacedMax,
      '\nEl maximo valor de Wards del Equipo Rojo colocados es:', redWardsPlacedMax, 
      '\nEl maximo valor del Total de Oro ganado del Equipo Azul es:', blueTotalGoldMax, 
      '\nEl maximo valor del Total de Oro ganado del Equipo Red es:', redTotalGoldMax)
print('-------------------------------------------------------------------------------\n')

# Bsucamos el minimo valor de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
blueWardsPlacedMin, redWardsPlacedMin, blueTotalGoldMin, redTotalGoldMin = a.apply(min)
print('El minimo valor de Wards del equipo azul colocados es:', blueWardsPlacedMin,
      '\nEl minimo valor de Wards del Equipo Rojo colocados es:', redWardsPlacedMin, 
      '\nEl minimo valor del Total de Oro ganado del Equipo Azul es:', blueTotalGoldMin, 
      '\nEl minimo valor del Total de Oro ganado del Equipo Red es:', redTotalGoldMin)
print('-------------------------------------------------------------------------------\n')

# Calculamos el conteo de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
blueWardsPlacedCount, redWardsPlacedCount, blueTotalGoldCount, redTotalGoldCount = a.apply(count)
print('El conteo de Wards del equipo azul colocados es:', blueWardsPlacedCount,
      '\nEl conteo de Wards del Equipo Rojo colocados es:', redWardsPlacedCount, 
      '\nEl conteo del Total de Oro ganado del Equipo Azul es:', blueTotalGoldCount, 
      '\nEl conteo del Total de Oro ganado del Equipo Red es:', redTotalGoldCount)
print('-------------------------------------------------------------------------------\n')

# Calculamos la moda de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
blueWardsPlacedMode, redWardsPlacedMode, blueTotalGoldMode, redTotalGoldMode = a.apply(mode)
print('El valor de la moda de Wards del equipo azul colocados es:', blueWardsPlacedMode,
      '\nEl valor de la moda de Wards del Equipo Rojo colocados es:', redWardsPlacedMode, 
      '\nEl valor de la moda del Total de Oro ganado del Equipo Azul es:', blueTotalGoldMode, 
      '\nEl valor de la moda del Total de Oro ganado del Equipo Red es:', redTotalGoldMode)
print('-------------------------------------------------------------------------------\n')

# Calculamos la media de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
blueWardsPlacedMean, redWardsPlacedMean, blueTotalGoldMean, redTotalGoldMean = a.apply(mean)
print('La media de Wards del equipo azul colocados es:', blueWardsPlacedMean,
      '\nLa media de Wards del Equipo Rojo colocados es:', redWardsPlacedMean,
      '\nLa media del Total de Oro ganado del Equipo Azul es:', blueTotalGoldMean, 
      '\nLa media del Total de Oro ganado del Equipo Red es:', redTotalGoldMean)
print('-------------------------------------------------------------------------------\n')

# Calculamos la varianza de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
blueWardsPlacedVar, redWardsPlacedVar, blueTotalGoldVar, redTotalGoldVar = a.apply(var)
print('La varianza de Wards del equipo azul colocados es:', blueWardsPlacedVar,
      '\nLa varianza de Wards del Equipo Rojo colocados es:', redWardsPlacedVar, 
      '\nLa varianza del Total de Oro ganado del Equipo Azul es:', blueTotalGoldVar, 
      '\nLa varianza del Total de Oro ganado del Equipo Red es:', redTotalGoldVar)
print('-------------------------------------------------------------------------------\n')

# Calculamos la desviacion estandar de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
blueWardsPlacedStd, redWardsPlacedStd, blueTotalGoldStd, redTotalGoldStd = a.apply(std)
print('La desviacion estandar de Wards del equipo azul colocados es:', blueWardsPlacedStd,
      '\nLa desviacion estandar de Wards del Equipo Rojo colocados es:', redWardsPlacedStd, 
      '\nLa desviacion estandar del Total de Oro ganado del Equipo Azul es:', blueTotalGoldStd, 
      '\nLa desviacion estandar del Total de Oro ganado del Equipo Red es:', redTotalGoldStd)
print('-------------------------------------------------------------------------------\n')

# Calculamos la asimetria de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
blueWardsPlacedSkew, redWardsPlacedSkew, blueTotalGoldSkew, redTotalGoldSkew = a.apply(skew)
print('La asimetria de Wards del equipo azul colocados es:', blueWardsPlacedSkew, 
      '\nLa asimetria de Wards del Equipo Rojo colocados es:', redWardsPlacedSkew,
      '\nLa asimetria del Total de Oro ganado del Equipo Azul es:', blueTotalGoldSkew,
      '\nLa asimetria del Total de Oro ganado del Equipo Red es:', redTotalGoldSkew)
print('-------------------------------------------------------------------------------\n')