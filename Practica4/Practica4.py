#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 4: DATA VISUALIZATION
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from scipy.stats import bartlett # prubea de igualdad de varianza
from scipy.stats import normaltest # prueba de normalidad
from scipy.stats import f_oneway #prueba ANDEVA una vía
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import scipy.stats

data = pd.read_csv('C:/Users/Admin/Desktop/Mineria-de-datos/lol_dataframe3.csv')
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

#Prueba de homocedasticidad
alfa = 0.05
Stat,p = bartlett(redGold,blueGold,redKills,blueKills)
print('p = {:g}'.format(p))
if p<alfa:
    print('No existen evidencias estadísticas para suponer igualdad de varianza ')
else:
    print('Existen evidencias estadísticas  para suponer igualdad de varianza')

#ANDEVA

# Ho: todas las medias son iguales
# Ha: al menos una de las medias es diferente
# Criterio: Fc < F entonces Ho es verdadero y si Fc >= F entonces Ho no es verdadero

Fc, p = f_oneway(redGold.values,blueGold.values,redKills.values,blueKills.values)

# Grados de libertad: k= numero de factores(4), N= numero de datos(104) numerador = k-1 <-(3-1) y el denominador = N-k <-(80-3)
de = 104-4
nu = 4-1

F= scipy.stats.f.ppf(q=1-0.05, dfn=nu, dfd=de)

if Fc < F:
    print('Fc = {:g}'.format(Fc), '<', 'F = {:g}'.format(F), 'p = {:g}'.format(p))
    print('No existen evidencias suficientes para rechazar Ho, por lo que podemos suponer que no hay diferencia entre medias')
else:
    print('Fc = {:g}'.format(Fc), '>=', 'F = {:g}'.format(F), 'p = {:g}'.format(p))
    print('Existen evidencias suficientes para rechazar Ho, por lo que podemos suponer que al menos una de las medias es diferentes')  

df = pd.DataFrame({'datos': np.concatenate([redGold.values,blueGold.values,redKills.values, blueKills.values]),
                   'factor':np.repeat(['redGold','blueGold','redKills', 'blueKills'],repeats=26)})

#Comparación multiple de tukey
tukey = pairwise_tukeyhsd(endog=df['datos'], 
                          groups=df['factor'],
                          alpha=0.05)
print(tukey)

data.boxplot(column=['blueKills','redKills'])
plot.show()
