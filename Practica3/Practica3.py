#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 3: DATA VISUALIZATION
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
from sys import path
path.append("../MINERIA-DE-DATOS")
import pandas as pd
import matplotlib.pyplot as plt
import Practica2.Practica2 as P2

P2.data

plt.figure(figsize=(20,20))
plt.subplot(1, 4, 1)
plt.scatter(P2.data['blueKills'], P2.data['blueTotalGold'], c='blue')
plt.title('EQUIPO AZUL', loc = "right", fontdict = {'fontsize':20, 'fontweight':'bold', 'color':'tab:blue'})
plt.xlabel('Asesinatos', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
plt.ylabel('Oro Total Ganado', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
plt.subplot(1, 4, 2)
plt.scatter(P2.data['blueTotalMinionsKilled'], P2.data['blueTotalGold'], c='blue')
plt.xlabel('Asesinatos', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
plt.ylabel('Total de Minions Asesinados', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
plt.subplot(1, 4, 3)
plt.scatter(P2.data['redKills'], P2.data['redTotalGold'], c='red')
plt.xlabel('Asesinatos', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:red'})
plt.ylabel('Oro Total Ganado', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:red'})
plt.title('EQUIPO ROJO', loc = "right", fontdict = {'fontsize':20, 'fontweight':'bold', 'color':'tab:red'})
plt.subplot(1, 4, 4)
plt.scatter(P2.data['redTotalMinionsKilled'], P2.data['redTotalGold'], c='red')
plt.xlabel('Total de Minions Asesinados', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:red'})
plt.ylabel('Oro Total Ganado', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:red'})

plt.show()


