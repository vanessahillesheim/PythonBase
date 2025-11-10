"""
Faça um programa que imprime os números pares de 1 a 200

Exemplo: 2,4,6,8,10
"""

numeros = range(1,201)

for n in numeros:
    par = n %2 == 0
    if par:
        print(n)
    else: 
        continue 

"""
Resolução do professor:

for num in range (1,201):
    if num %2 !=0:
        continue
    print(num)
"""