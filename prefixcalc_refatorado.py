#!/usr/bin/env python3
"""
Calculadora Prefix
"""
__version__ = "0.1.1"
__author__ = "Vanessa Hillesheim"

import sys
import os
from datetime import datetime

argumentos = sys.argv[1:]

valida_operacoes = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b, 
    "div": lambda a, b: a / b
}

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
usuario = os.getenv('USER', 'anonymous')

while True:
    # Reset dos argumentos para permitir nova entrada
    if not argumentos or len(argumentos) != 3:
        if argumentos:
            print("Número de argumentos inválido")
            print("Exemplo: 'sum 5 5'")
            argumentos = []  # Reset para pedir novos valores
            continue
        
        operacao = input("Digite a operação: ")
        n1 = input("Digite o 1º número: ")
        n2 = input("Digite o 2º número: ")
        argumentos = [operacao, n1, n2]

    operacao, *nums = argumentos

    if operacao not in valida_operacoes:
        print("Operação inválida")
        print("Operações válidas:", list(valida_operacoes.keys()))
        argumentos = []  # Reset para tentar novamente
        continue

    # Validação dos números
    valida_nums = []
    for num in nums:
        if not num.replace(".", "").replace("-", "").isdigit():  # Adicionado tratamento para negativo
            print(f"Número inválido {num}")
            argumentos = []  # Reset
            break
        if "." in num:
            num = float(num)
        else: 
            num = int(num)
        valida_nums.append(num)
    else:  # Executa apenas se o for não foi interrompido por break
        if len(valida_nums) != 2:
            print("Número de argumentos inválido")
            argumentos = []
            continue

        n1, n2 = valida_nums

        # Cálculo dentro do try para capturar erros matemáticos
        try:
            resultado = valida_operacoes[operacao](n1, n2)
            print(f"O resultado é {resultado:.2f}")

            # Salvar no log
            try:
                with open(filepath, "a") as file_:
                    file_.write(f"{timestamp} - {usuario} - {operacao}, {n1}, {n2} = {resultado}\n")
            except PermissionError as e:
                print(f"Erro ao salvar log: {e}")

        except ZeroDivisionError:
            print("Erro: Divisão por zero!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

    # Reset dos argumentos para próxima iteração
    argumentos = []
    
    # Verificar se usuário quer continuar
    if input("Pressione enter para continuar ou qualquer tecla para sair: "):
        break