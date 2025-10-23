#!/usr/bin/env python3

"""
Fazer um e-mail para clientes usando interpolação de dados e variável multi linhas

para executar o arquiv, no ipython digitar: python interpolacao.py emails.txt email_tmpl.txt
"""

__version__ = "0.1.1"
__author__ = "Vanessa"

# %s → string
# %d → número inteiro (decimal)
# %f → número de ponto flutuante (float)


#ajustano a utilização do arquivo txt com endreço dos e-mails
import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print(f"informe o nome do arquivo de e-mails.")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]
path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

for line in open(filepath):
    nome, email = line.split(",")
    print(f"Enviando e-mail para: {email}")
    print(
        open(templatepath).read()
        % {
            "nome": nome,
            "produto": "caneta",
            "texto": "escrever com tinta molhada",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
           
        }
    )
    print("-" *50)    


# concatenação com %s (usado em logging)
msg = "Olá, %s! Você é o player nº %03d e tens %.3f pontos!"
msg = msg % ("Vanessa", 2, 615.16)
print(msg)

# interpolação com {} (usando str.format — útil em textos longos)
msg = "Olá, {}! Você é o player nº {:03d} e tens {:.3f} pontos!"
msg = msg.format("Vanessa", 2, 615.16)
print(msg)

# interpolação com f-strings (forma moderna e recomendada)
nome = "Vanessa"
player = 2
pontos = 615.16

msg = f"Olá, {nome}! Você é o player nº {player:03d} e tens {pontos:.3f} pontos!"
print(msg)

# printando emoji com código Unicode (usando code points)
print("\U0001F43C")  # 🐼
print("\U0001F600")  # 😀

# printando emoji com nome Unicode
print("\N{RED APPLE}")      # 🍎
print("\N{GREEN APPLE}")    # 🍏