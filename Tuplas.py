print("declaração de dupla sem parênteses - operação de empacotamento")
tupla1 = 1, 2, 3
print("tupla = ", tupla1)

#DECLARAÇÃO SEM PARÊNTESES
print ("\nlaço for para percorrer em tupla")
for i in tupla1:
     print(i)
     
#laço para percorrer uma tupla     
print("\ntupla utilizada para desempacotar valores")
x, y = 1, 3
print("x = ", x, "\ny =", y)
print("\ntrocando os valores das variáveis x e y: \nx, y = y, x")
x, y = y, x
print("valores trocados de x e y: x = ", x, "\ty = ", y)

print("\nCRIAÇAO DE TUPLA A PARTIR DE LISTA: função tuple(lista)")
lista0 = [8, 9, 10]
tupla3 = tuple(lista0)
print("tupla gerada a partir de lista = ", tupla3)

print("nLista contida em Tupla:")
tupla4 = (17, 3, -6,[-2, 0, -1])
print("\ntamanho da tupla4 = ", len(tupla4))
for j, k in enumerate(tupla4):
    print(f"elemento{j} de tupla4: {k}")
print("\nadicionando elemento À parte da lista da tupla:")
tupla4[3].append(-11)
print("\ntupla4 com elemento adicionado À lista:", tupla4)
