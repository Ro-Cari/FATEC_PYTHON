# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:15:32 2022

@author: RoCari
"""
from matplotlib import pyplot as plt
Anos = [1, 2, 4, 8, 16, 1990, 1995, 2000, 2005]
População = [199.76, 206.47, 209.80, 260.00, 300.33, 388.64, 400.00, 444.44, 470.99]

#Gráfico de barras
#Barras tem o tamanho padrão de 0.8: deve-se adicionar 0.1 às coordenadas
#à esquerda para que cada barra seja centralizada
x = [i + 0.1 for i, _ in enumerate(Anos)]

#criação do gráfico
plt.bar(x, População, color = "pink")

#Label no eixo Y
plt.ylabel("em milhares de pessoas")

#Título
plt.title("Variação da população de Santos por Ano * 1000")

#Valoração do eixo x com os valores dos anos
plt.xticks( [i + 0.5 for i, _ in enumerate(Anos)], Anos)

#Controi gráfico
plt.show()