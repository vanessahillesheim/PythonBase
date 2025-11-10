"""
venv\Scripts\Activate.ps1
Faça um programa de terminal que exibe ao usuário uma lista dos quartos disponíveis para alugar e o preço de cada quarto. Esta informação está disponível em um arquivo texto, separado por vírgulas:

'quarto.txt'
# código, nome, preço
1, Suíte Master, 500
2, Quarto Família, 200
3, Quarto Single, 100
4, Quarto Simples, 50

O programa pergunta ao usuário o nome, qual  o número do quarto a ser reservado e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas.
'reservas.txt'
# cliente, quarto, dias
Bruno, 3, 12

Se outro usuário tentar reservar o mesmo quarto, o programa deve exibir uma mensagem informando que "já está reservado".
"""

#para iniciar, precisamos ler o arquivo reservas.txt, para saber se há algum quarto vago/reservado

import sys
import logging

RESERVAS_FILE = "reservas.txt"
QUARTOS_FILE = "quartos.txt"

#Acesso ao Banco de Dados
ocupados = {} #acumulador que começa vazio

try: #se o arquivo reservas.txt não existir
    for line in open(RESERVAS_FILE):
        nome_cliente, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = { #convertendo para inteiros o nº de dias
            "nome_cliente": nome_cliente,
            "dias": dias
        }
except FileNotFoundError:
    logging.error("arquivo %s não existe!", RESERVAS_FILE)
    sys.exit(1)


quartos = {} #acumulador
try: #se o arquivo reservas.txt não existir
    for line in open(QUARTOS_FILE):
       num_quarto, nome_quarto, preco = line.strip().split(",")
       quartos[int(num_quarto)] = { 
            "nome_quarto": nome_quarto,
            "preco": float(preco),
            "disponivel": False if int(num_quarto) in ocupados else True
        }
except FileNotFoundError:
    logging.error("arquivo %s não existe!", QUARTOS_FILE)
    sys.exit(1)

#Programa principal
print("Reseras no Hotel Python da Linux Tips")
print("-"*40)

if len(ocupados) == len(quartos):
    print("Hotel está lotado, volte depois")
    sys.exit(0)

nome_cliente = input(f"Qual é o seu nome?").strip()

print("Lista de Quartos")
print("Número - Nome do Quarto   - Preço     - Disponível?")
for num_quarto, dados_quarto in quartos.items():
    nome_quarto = dados_quarto["nome_quarto"]
    preco = dados_quarto["preco"]
    disponivel = "❌"if not dados_quarto["disponivel"] else "👍"
    print(f"{num_quarto:<6} - {nome_quarto:<16} - R${preco:<7.2f} - {disponivel}")

    #parei em 53:40
