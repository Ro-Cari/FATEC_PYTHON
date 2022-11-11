PI = 3.1416
print("\n")
def converte_radiano(graus):
    PI = 3.14
    radianos = (graus*PI)/180
    print("\nO valor da váriavel local PI = ", PI)
    return radianos


print("90°  equivale a ", converte_radiano(90), "radianos")
print("180°  equivale a ", converte_radiano(180), "radianos")
print("270°  equivale a ", converte_radiano(270), "radianos")
print("360°  equivale a ", converte_radiano(360), "radianos")

print("\n VALOR GLOBAL DE PI NÃO É ALTERADOPELA FUNÇÃO 'converte_radiano' \ne continua PI = ", PI)