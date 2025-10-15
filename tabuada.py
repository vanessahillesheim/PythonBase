#!/usr/bin/env python
"""
Imprime tabuada de 1 ai 10.

Tabuada do 1
1
2
3
...
__________________
Tabuada do 2
1
2
3
...
"""

__version__ = "0.0.1"
__author__ = "Vanessa"

numeros = list(range(1,11))

for n in numeros:
    print("Tabuada do:", n)
    for numero in numeros:
        resultado = n * numero
        print(f"{n} x {numero} = {resultado}")
    print("-"*15)

