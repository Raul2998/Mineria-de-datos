#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 4: DATA VISUALIZATION
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

import numpy as np
import pandas as pd
from scipy.stats import bartlett # prubea de igualdad de varianza
from scipy.stats import normaltest # prueba de normalidad
from scipy.stats import f_oneway #prueba ANDEVA una vía

data = pd.read_csv('C:/Users/raulh/OneDrive/Documentos/Mineria-de-datos/lol_dataframe3.csv')
redGold = data['redTotalGold']
blueGold = data['blueTotalGold']
redKills = data['redKills']
blueKills = data['blueKills']

# Prueba de normalidad 1 
S,p = normaltest(redGold)
alfa = 0.05
print('p = {:g}'.format(p))

if p<alfa:
    print('No existen evidencias estadísticas para suponer normalidad')
else:
    print('Existen evidencias estadísticas para suponer normalidad')

# Prueba de normalidad 2
S,p = normaltest(blueGold)
alfa = 0.05
print('p = {:g}'.format(p))

if p<alfa:
    print('No existen evidencias estadísticas para suponer normalidad')
else:
    print('Existen evidencias estadísticas para suponer normalidad')

# Prueba de normalidad 3 
S,p = normaltest(redKills)
alfa = 0.05
print('p = {:g}'.format(p))

if p<alfa:
    print('No existen evidencias estadísticas para suponer normalidad')
else:
    print('Existen evidencias estadísticas para suponer normalidad')

# Prueba de normalidad 4
S,p = normaltest(blueKills)
alfa = 0.05
print('p = {:g}'.format(p))

if p<alfa:
    print('No existen evidencias estadísticas para suponer normalidad')
else:
    print('Existen evidencias estadísticas para suponer normalidad')