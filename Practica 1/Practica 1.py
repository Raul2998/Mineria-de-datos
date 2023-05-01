# ------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 1: DATA CLEANING
# Importacion de librerías
import pandas as pd
import matplotlib.pyplot as plt


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
# PRACTICA 3: DATA VISUALIZATION
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

print('---------------------------------------------------------------------------------------------------\n\n\n\n\n\n',
      'PRACTICA 3: DATA VISUALIZATION',
      '\n\n\n\n\n\n---------------------------------------------------------------------------------------------------')

scores = ['gameDuration', 'queueId', 'seasonId']
for i in range(0,3):
    plt.scatter(x = data['gameId'], y = data[scores[i]])
plt.show()
