#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# PRACTICA 6: FORECASTING
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/raulh/OneDrive/Documentos/Mineria-de-datos/Practica6/forecasting.csv')

print(data.head)
print('-------------------------------------------------------------------------------\n')

# Creamos nuestro plot inicial
plt.figure(figsize=(12, 6))
plt.plot(data.index,data['Monthly beer production'])
plt.xlabel('Periodos', fontsize=14)
plt.ylabel('Produccion', fontsize=14)
plt.title('Plot Inicial')
plt.show()

# Preparamos los datos añadiendo una colummna con solo el año
data['year'] = data['Month'].apply(lambda x:pd.Timestamp(x).strftime('%Y'))
print(data)
print('-------------------------------------------------------------------------------\n')

# Creamos un nuevo data set con el indice por año y agrupado de menor a mayor
anual = data.groupby(by=['year']).sum().reset_index()
print(anual)
print('-------------------------------------------------------------------------------\n')

# Plotting el nuevo dataset acomodado de forma anual
plt.figure(figsize=(12, 6))
plt.plot(anual.index,anual['Monthly beer production'], '-o')
plt.xlabel('Periodos', fontsize=14)
plt.ylabel('Produccion', fontsize=14)
plt.title('Plot Anual')
plt.show()

# Promedio Media Movil
anual['MA'] = anual['Monthly beer production'].rolling(window=3).mean().shift(1)
print(anual)
print('-------------------------------------------------------------------------------\n')

# Plotting forecast con el Movile Average aplicado
#plt.figure(figsize=(12, 6))
#plt.plot(anual.index, anual['Monthly beer production'], '-o', color = 'red', label = 'data')
#plt.plot(anual.index, anual['MA'], '-o', color = 'blue', label = 'forecast')
#plt.xlabel('Periodos', fontsize=14)
#plt.ylabel('Produccion', fontsize=14)
#plt.legend(loc = 'best')
#plt.show()

# Agregamos una nueva fila a nuestro dataframe para hacer el forecasting
anual.loc[len(anual)] = [int(anual.iloc[len(anual)-1][0])+1,0,0]
print(anual)
print('-------------------------------------------------------------------------------\n')

# Dando formato a nuestro dataframe y hacemos el forecasting a esta nueva fila
anual['MA'] = anual['Monthly beer production'].rolling(window=3).mean().shift(1)
anual['year'] = anual['year'].astype(int)
anual['Monthly beer production'] = anual['Monthly beer production'].astype(float)
anual['MA'] = anual['MA'].astype(float)
print(anual)
print('-------------------------------------------------------------------------------\n')

# Plotting data y forecast
plt.figure(figsize=(12, 6))
plt.plot(anual['year'][:-1], anual['Monthly beer production'][:-1], '-o', color = 'red', label = 'data')
plt.plot(anual['year'], anual['MA'], '-o', color = 'blue', label = 'forecast')
plt.xlabel('Años', fontsize=14)
plt.ylabel('Produccion', fontsize=14)
plt.legend(loc = 'best')
plt.show()