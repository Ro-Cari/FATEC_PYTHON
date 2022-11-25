# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 11:11:46 2022

@author: LAB54
"""


import math
from matplotlib import pyplot as plt

def equacao_2ºgrau(a, b, c):
    delta = pow(b, 2) - 4*a*c
    if delta < 0:
        return "raiz negativa, solução é imaginária"
    else:
        raiz_delta = math.sqrt(delta)
        x1 =( b + raiz_delta)/2*a
        x2 = (-b - raiz_delta)/2*a
        resultado = x1, x2 #raizes armazenadas em uma tupla
        return resultado

def parábola (a, b, c):
    y = []
    for x in range (-2, 8):
        y.append(a*pow(x,2) + b*x +c)
    x = [x for x in range (-2, 8)]
    
    #Cria um gráfico de linha, y -> ordenadas, x -> abscissas
    plt.plot(x, y, color = 'orange', marker = 'o', linestyle = 'solid')
    
    #Cria as linhas da grade
    plt.grid(b = None, which = 'major', axis = 'both')
    
    #Estabelece os limites inferior e superior do eixo y
    plt.ylim(-10, 3)
    
    #Título do gráfico
    plt.title("Equação do 2º Grau -> função quadrática")
    
    #Comentário no eixo X
    plt.xlabel("eixo x -> abscissas")
    
     #Comentário no eixo Y
    plt.ylabel("eixo y -> ordenadas")
    
    #Controi gráfico
    plt.show()
    
#raizes_equação = tupla com 2 elementos

raízes_equação = equacao_2ºgrau(-1, 6, -8)
print ("REsultado da Equação do 2º Grau: ")
print("x1 = ", raízes_equação[0])
print("x2 = ", raízes_equação[1])
parábola(-1, 6, -8)