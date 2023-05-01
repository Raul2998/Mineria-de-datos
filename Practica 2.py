#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 2: DESCRIPTIVE STATISTICS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/raulh/OneDrive/Documentos/Tareas/Mineria de datos/lol_dataframe2.csv')
# Visualizamos nuestro dataframe por sus categorias
data.info()

# Calculamos la suma individual de las columnas gameDuration, queueId y seasonId
print ('La suma individual de las columnas gameDuration, queueId y seasonId es: \n', data[['gameDuration', 'queueId', 'seasonId']].sum()) 

# Creamos una funcion donde sacamos la media de las columnas: gameDuration, queueId y seasonId
def media(data):
    mean = data.mean()
    return mean

sel_cols = ['gameDuration', 'queueId', 'seasonId']

b = data[sel_cols]

gameDuration, queueId, seasonId = b.apply(media)

print('La media de gameDuration, queueId, seasonId es:', gameDuration, queueId, seasonId)

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