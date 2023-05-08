#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 4: DATA VISUALIZATION
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
from sys import path
path.append("../MINERIA-DE-DATOS")
from Practica2.Practica2 import data
import numpy as np
import pandas as pd
from scipy.stats import bartlett # prubea de igualdad de varianza
from scipy.stats import normaltest # prueba de normalidad
from scipy.stats import f_oneway #prueba ANDEVA una vía



# Prueba de normalidad 1 
S,p = normaltest(data['blueKills'])
alfa = 0.05
print('p = {:g}'.format(p))

if p<alfa:
    print('No existen evidencias estadísticas para suponer normalidad')
else:
    print('Existen evidencias estadísticas para suponer normalidad')
