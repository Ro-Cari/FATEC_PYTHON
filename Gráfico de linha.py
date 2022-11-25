"""
Created on Fri Nov 25 10:00:02 2022

@author: RoCari
"""

from matplotlib import pyplot as plt
Anos = [1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005]
População = [199.76, 206.47, 209.80, 260.00, 300.33, 388.64, 400.00, 444.44, 470.99]

#criação do gráfuco
plt.plot(Anos, População, color = "pink", marker="o", linestyle ="solid")

#Título
plt.title("Variação da população de Santos por Ano * 1000")

#Label no eixo Y
plt.ylabel("em milhares de pessoas")

#Controi gráfico
plt.show()