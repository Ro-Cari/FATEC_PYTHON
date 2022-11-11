PI = 3.1416
variavel_global = "PI"

def area_circunferencia(raio):
    print ("uso da váriavel global", variavel_global, " = ", PI)
    return PI*pow(raio,2)

def comprimento_circunferencia(diametro):
    print ("uso da variavel global", variavel_global, " = ", PI)
    return PI*diametro

print("A circunferência de raio 3 tem área = ", area_circunferencia(3))
print("A cirncuferÊncia de diâmetro 6  tem comprimento = ", comprimento_circunferencia(6))
