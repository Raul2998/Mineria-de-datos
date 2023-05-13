#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 2: DESCRIPTIVE STATISTICS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/raulh/OneDrive/Documentos/Mineria-de-datos/lol_dataframe2.csv')
sel_cols = ['blueKills', 'redKills', 'blueTotalGold','redTotalGold']
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

# Visualizamos nuestro dataframe por sus categorias
data.info()
print('-------------------------------------------------------------------------------\n')

# Calculamos la suma individual de las columnas blueWins y redWins
blueWins, redWins = b.apply(suma)
print ('La suma de las Victorias del Equipo Azul es:', blueWins, 
       '\nLa suma de las Victorias del Equipo Red es:', redWins)
print('-------------------------------------------------------------------------------\n')

# Buscamos el maximo valor de las columnas: blueKills, redKills, blueTotalGold, redTotalGold
blueKillsMax, redKillsMax, blueTotalGoldMax, redTotalGoldMax = a.apply(max)
print('El maximo valor de Asesinatos del equipo azul colocados es:', blueKillsMax,
      '\nEl maximo valor de Asesinatos del Equipo Rojo colocados es:', redKillsMax, 
      '\nEl maximo valor del Total de Oro ganado del Equipo Azul es:', blueTotalGoldMax, 
      '\nEl maximo valor del Total de Oro ganado del Equipo Red es:', redTotalGoldMax)
print('-------------------------------------------------------------------------------\n')

# Bsucamos el minimo valor de las columnas: blueKills, redKills, blueTotalGold, redTotalGold
blueKillsMin, redKillsMin, blueTotalGoldMin, redTotalGoldMin = a.apply(min)
print('El minimo valor de Asesinatos del equipo azul colocados es:', blueKillsMin,
      '\nEl minimo valor de Asesinatos del Equipo Rojo colocados es:', redKillsMin, 
      '\nEl minimo valor del Total de Oro ganado del Equipo Azul es:', blueTotalGoldMin, 
      '\nEl minimo valor del Total de Oro ganado del Equipo Red es:', redTotalGoldMin)
print('-------------------------------------------------------------------------------\n')

# Calculamos el conteo de las columnas: blueKills, redKills, blueTotalGold, redTotalGold
blueKillsCount, redKillsCount, blueTotalGoldCount, redTotalGoldCount = a.apply(count)
print('El conteo de Asesinatos del equipo azul colocados es:', blueKillsCount,
      '\nEl conteo de Asesinatos del Equipo Rojo colocados es:', redKillsCount, 
      '\nEl conteo del Total de Oro ganado del Equipo Azul es:', blueTotalGoldCount, 
      '\nEl conteo del Total de Oro ganado del Equipo Red es:', redTotalGoldCount)
print('-------------------------------------------------------------------------------\n')

# Calculamos la moda de las columnas: blueWardsPlaced, redKills, blueTotalGold, redTotalGold
blueKillsMode, redKillsMode, blueTotalGoldMode, redTotalGoldMode = a.apply(mode)
print('El valor de la moda de Asesinatos del equipo azul colocados es:', blueKillsMode,
      '\nEl valor de la moda de Asesinatos del Equipo Rojo colocados es:', redKillsMode, 
      '\nEl valor de la moda del Total de Oro ganado del Equipo Azul es:', blueTotalGoldMode, 
      '\nEl valor de la moda del Total de Oro ganado del Equipo Red es:', redTotalGoldMode)
print('-------------------------------------------------------------------------------\n')

# Calculamos la media de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
blueKillsMean, redKillsMean, blueTotalGoldMean, redTotalGoldMean = a.apply(mean)
print('La media de Asesinatos del equipo azul colocados es:', blueKillsMean,
      '\nLa media de Asesinatos del Equipo Rojo colocados es:', redKillsMean,
      '\nLa media del Total de Oro ganado del Equipo Azul es:', blueTotalGoldMean, 
      '\nLa media del Total de Oro ganado del Equipo Red es:', redTotalGoldMean)
print('-------------------------------------------------------------------------------\n')

# Calculamos la varianza de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
blueKillsVar, redKillsVar, blueTotalGoldVar, redTotalGoldVar = a.apply(var)
print('La varianza de Asesinatos del equipo azul colocados es:', blueKillsVar,
      '\nLa varianza de Asesinatos del Equipo Rojo colocados es:', redKillsVar, 
      '\nLa varianza del Total de Oro ganado del Equipo Azul es:', blueTotalGoldVar, 
      '\nLa varianza del Total de Oro ganado del Equipo Red es:', redTotalGoldVar)
print('-------------------------------------------------------------------------------\n')

# Calculamos la desviacion estandar de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
blueKillsStd, redKillsStd, blueTotalGoldStd, redTotalGoldStd = a.apply(std)
print('La desviacion estandar de Asesinatos del equipo azul colocados es:', blueKillsStd,
      '\nLa desviacion estandar de Asesinatos del Equipo Rojo colocados es:', redKillsStd, 
      '\nLa desviacion estandar del Total de Oro ganado del Equipo Azul es:', blueTotalGoldStd, 
      '\nLa desviacion estandar del Total de Oro ganado del Equipo Red es:', redTotalGoldStd)
print('-------------------------------------------------------------------------------\n')

# Calculamos la asimetria de las columnas: blueWardsPlaced, redWardsPlaced, blueTotalGold, redTotalGold
blueKillsSkew, redKillsSkew, blueTotalGoldSkew, redTotalGoldSkew = a.apply(skew)
print('La asimetria de Asesinatos del equipo azul colocados es:', blueKillsSkew, 
      '\nLa asimetria de Asesinatos del Equipo Rojo colocados es:', redKillsSkew,
      '\nLa asimetria del Total de Oro ganado del Equipo Azul es:', blueTotalGoldSkew,
      '\nLa asimetria del Total de Oro ganado del Equipo Red es:', redTotalGoldSkew)
print('-------------------------------------------------------------------------------\n')