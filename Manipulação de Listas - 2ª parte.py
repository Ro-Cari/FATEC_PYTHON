# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

comentario = ["As formigas","trabalham","durante","o ano inteiro","As cigarras","aparecem", "no verão."]
dimensao_comentario = len(comentario)
i = 0
while i < dimensao_comentario:
    print(comentario[i]) 
    i += 1
print ('\nsó as formigas!')
comentario_formigas = comentario[0:4]
dimensao_comentario_formigas = len(comentario_formigas)
j =0 
while j < dimensao_comentario_formigas:
    print(comentario_formigas[j])

    j += 1
print('\nsó as cigarras!')
comentario_cigarras = comentario[4:7]
dimensao_comentario_cigarras = len(comentario_cigarras)
k = 0
while k < dimensao_comentario_cigarras:
    print(comentario_cigarras[k])
    k += 1