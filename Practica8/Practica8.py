import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('C:/Users/raulh/OneDrive/Documentos/Mineria-de-datos/lol_dataframe2.csv')

# Creando eje X y eje Y
x = data['blueKills']
y = data['blueTotalGold']

# Crear matriz de características
X = np.array(list(zip(x, y)))

# Aplicar el algoritmo K-Means
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

# Obtener las etiquetas de los clusters
labels = kmeans.labels_

# Visualizar los clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='red', marker='x')
plt.xlabel('Asesinatos', fontsize=14)
plt.ylabel('Oro', fontsize=14)
plt.show()