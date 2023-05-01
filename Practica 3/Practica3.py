#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 3: DATA VISUALIZATION
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import pandas as pd
import matplotlib.pyplot as plt
from Practica2.py import col 

data = pd.read_csv('C:/Users/raulh/OneDrive/Documentos/Tareas/Mineria de datos/lol_dataframe2.csv')

scores = ['gameDuration', 'queueId', 'seasonId']
for i in range(0,3):
    plt.scatter(x = data['gameId'], y = data[scores[i]])
plt.show()
