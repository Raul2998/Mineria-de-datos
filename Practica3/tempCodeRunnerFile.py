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
P2.gold
P2.wards

for i in range(0,2):
    plt.scatter(x = P2.data['gameId'], y = P2.data[P2.gold[i]])
plt.show()

for i in range(0,2):
    plt.scatter(x = P2.data['gameId'], y = P2.data[P2.wards[i]])
plt.show()
