"""
Exemplos de funções
"""

## f(x) = 5*(x/2)
#como escrever esta função em python?

def f(x):
    return 5 * (x / 2) # / - resultado da divisão será decimal
print(f(10))

#------------------------------------------------------------------------------
# // - resultado da divisão será número inteiro
def f(x):
    result = 5 * (x // 2)
    return result
valor = f(10)
print(valor)

#------------------------------------------------------------------------------
def print_in_upper(text):
    print(text.upper())
print_in_upper("vanessa")

#------------------------------------------------------------------------------
#Fórmula de Heron = calcula a área de triângulo escaleno (com lados diferentes)

from math import sqrt #biblioteca de raiz quadrada

def heron(a,b,c):
    perimetro = a+b+c
    sp = perimetro/2 #sp = semiperimetro
    area = sp * (sp-a)*(sp-b)*(sp-c)
    return area ** 0.5 

#potenciação é o contrário da radiciação
# na raiz quadrada de 4, o expoente é 1/2 = 4 ¹/² = 2
# potenciação é 2²

area_triangulo = heron(3,4,5)
print(area_triangulo)

#usando a fórmula para calcular a área de vários triângulos
triangulos= [
             (3,4,5),
             (5,12,13), 
             (8,15,17),
             (12,35,37),
             (3,4,5),
             (5,12,13), 
             (8,15,17),
             (12,35,37),
             ]

for t in triangulos:
    area = heron(t[0], t[1], t[2])
    print(f"A área dos triângulo é: {area}")

#------------------------------------------------------------------------------
#Usando a fórmula heron com parêmtros e map

print("-"*42)
def heron2(params):
    return heron(*params)

print(map(heron2, triangulos))

for t in triangulos:
    area = heron2(t)
    print(f"A área dos triângulo é: {area}")

print(list(map(heron2, triangulos)))