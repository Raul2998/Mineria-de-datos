#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 3: DATA VISUALIZATION
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
from sys import path
path.append("../MINERIA-DE-DATOS")
import pandas as pd
import matplotlib.pyplot as plt
from Practica2.Practica2 import data

plt.figure(figsize=(20,20))
plt.subplot(1, 4, 1)
plt.scatter(data['blueKills'], data['blueTotalGold'], c='blue')
plt.title('EQUIPO AZUL', loc = "right", fontdict = {'fontsize':20, 'fontweight':'bold', 'color':'tab:blue'})
plt.xlabel('Asesinatos', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
plt.ylabel('Oro Total Ganado', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
plt.subplot(1, 4, 2)
plt.scatter(data['blueTotalMinionsKilled'], data['blueTotalGold'], c='blue')
plt.xlabel('Total de Minions Asesinados', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
plt.ylabel('Oro Total Ganado', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
plt.subplot(1, 4, 3)
plt.scatter(data['redKills'], data['redTotalGold'], c='red')
plt.xlabel('Asesinatos', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:red'})
plt.ylabel('Oro Total Ganado', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:red'})
plt.title('EQUIPO ROJO', loc = "right", fontdict = {'fontsize':20, 'fontweight':'bold', 'color':'tab:red'})
plt.subplot(1, 4, 4)
plt.scatter(data['redTotalMinionsKilled'], data['redTotalGold'], c='red')
plt.xlabel('Total de Minions Asesinados', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:red'})
plt.ylabel('Oro Total Ganado', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:red'})
plt.show()


