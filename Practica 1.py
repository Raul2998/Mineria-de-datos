# ------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 1: DATA CLEANING
# Importacion de librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Lectura del csv e impresion del header
data = pd.read_csv('C:/Users/raulh/OneDrive/Documentos/Tareas/Mineria de datos/lol_dataframe.csv')
print(data.shape,data.head())

# Veamos el dataset por sus variables categóricas y numéricas
data.info()

# Dropeamos las columnas gameCreation, mapId, status.message y status.status_code ya que no contienen informacion o no son relevantes 
# y verificamos que se hayan eliminado
data.drop(columns=['gameCreation','status.message', 'status.status_code', 'mapId'], inplace=True)
print('---------------------------------------------------------------------------------------------------\n', 
      data.shape, 
      '\n---------------------------------------------------------------------------------------------------')

# Conteo de los niveles en las diferentes columnas categóricas
cols_cat = ['gameMode','gameType','gameVersion', 'participantIdentities', 'participants', 'platformId']
for col in cols_cat:
        print(f'Columna {col}: {data[col].nunique()} subniveles')
        
# Se dropean la columna gameType y plataformId ya que contiene el mismo valor en todas las filas
print(f'Tamaño del set antes de eliminar las columunas gameType y plataformId: {data.shape}')
data.drop(columns=['gameType', 'platformId'], inplace=True)
print(f'Tamaño del set después de eliminar las  columunas gameType y plataformId: {data.shape}')

# Conteo de los niveles en las diferentes columnas numericas 
print('---------------------------------------------------------------------------------------------------\n',
      data.describe(), 
      '\n---------------------------------------------------------------------------------------------------')
# Como la desviacion estandar es diferente de 0 entonces no se elimina ninguna columna numerica

# Se dropean las posibles filas repetidas
print(f'Tamaño del set antes de eliminar las filas repetidas: {data.shape}')
data.drop_duplicates(inplace=True)
print(f'Tamaño del set después de eliminar las filas repetidas: {data.shape}')

# Visualizamos nuestro dataframe limpio
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------\n', 
      data.head(),
      '\n-----------------------------------------------------------------------------------------------------------------------------------------------------------')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 2: DESCRIPTIVE STATISTICS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

print('---------------------------------------------------------------------------------------------------\n\n\n\n\n\n',
      'PRACTICA 2: DESCRIPTIVE STATISTICS',
      '\n\n\n\n\n\n---------------------------------------------------------------------------------------------------')

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

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 3: DATA VISUALIZATION
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

print('---------------------------------------------------------------------------------------------------\n\n\n\n\n\n',
      'PRACTICA 3: DATA VISUALIZATION',
      '\n\n\n\n\n\n---------------------------------------------------------------------------------------------------')

scores = ['gameDuration', 'queueId', 'seasonId']
for i in range(0,3):
    plt.scatter(x = data['gameId'], y = data[scores[i]])
plt.show()
