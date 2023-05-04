
plt.figure(figsize=(15,15))
plt.subplot(1,2,1)
plt.scatter(P2.data['blueKills'], P2.data['blueTotalGold'])
plt.title('Equipo Azul')
plt.subplot(1,2,2)
plt.scatter(P2.data['redKills'], P2.data['redTotalGold'])
plt.title('Equipo Rojo')
plt.show()