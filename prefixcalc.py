#!/usr/bin/env python3
"""
Calculadora Prefix

Operações: 
sum -> +
sub -> -
mul -> *
div -> /

Funcionamento:
3 argumentos para exibir o resultado
[operação] [n1] [n2]

Uso:
$ prefixcalc.py sum 5 2 7
$ prefixcalc.py mul 10 5 50
"""
__version__ = "0.1.0"
__author__ = "Vanessa Hillesheim"


""" Minha resolução
operacao = input("Digite a operação desejada: sum para somar; sub para subtrair; mul para multiplicar e div para dividir: ")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

try:
    if operacao == "sum":
        resultado = n1 + n2
    elif operacao == "sub":
        resultado = n1 - n2
    elif operacao == "mul":
        resultado = n1 * n2
    elif operacao == "div":
        resultado = n1 / n2
    
    print(f"O resultado é {resultado:.2f}")
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
"""

import sys
argumentos = sys.argv[1:]

if not argumentos:
    operacao = input("Digite a operação: ")
    n1 = input("Digite o 1º número: ")
    n2 = input("Digite o 2º número: ")
    argumentos = [operacao, n1, n2]
elif len(argumentos) != 3:
    print("Número de argumentos inválido")
    print("Exemplo: 'sum 5 5 '")
    sys.exit(1)

operacao, *nums = argumentos

valida_operacoes = ("sum", "sub", "mul", "div")
if operacao not in valida_operacoes:
    print("Operação inválida")
    print(valida_operacoes)
    sys.exit(1)

#validacao dos numeros digitados
valida_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else: 
        num = int(num)
    valida_nums.append(num)

n1, n2 = valida_nums
try:
    if operacao == "sum":
        resultado = n1 + n2
    elif operacao == "sub":
        resultado = n1 - n2
    elif operacao == "mul":
        resultado = n1 * n2
    elif operacao == "div":
        resultado = n1 / n2
    
    print(f"O resultado é {resultado:.2f}")
except ZeroDivisionError:
    print("Erro: Divisão por zero!")

