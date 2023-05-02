#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 3: DATA VISUALIZATION
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
from sys import path
path.append("../MINERIA-DE-DATOS")
import pandas as pd
import matplotlib.pyplot as plt
from Practica2.Practica2 import *
import Practica2.Practica2 as P2

P2.data
P2.sel_cols
P2.wards
P2.gold

plt.figure(figsize=(10,6))
plt.subplot(131)
plt.bar(P2.data['gameId'], P2.data['blueWin'])
plt.subplot(131)
plt.bar(P2.data['gameId'], P2.data['redWin'])
plt.show()

