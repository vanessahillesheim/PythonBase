#!/usr/bin/env python3

"""
Fazer um e-mail para clientes usando interpolação de dados e variável multi linhas
"""

__version__ = "0.0.1"
__author__ = "Vanessa"

# %s → string
# %d → número inteiro (decimal)
# %f → número de ponto flutuante (float)

email_tmpl = """
Olá, %(nome)s!
Tem interesse em comprar %(produto)s?
Este produto é ótimo para %(texto)s! 
Clique agora no link %(link)s e adquira! 
Resta apenas %(quantidade)d no estoque!
Preço promocional para você é R$%(preco).2f! Aproveite!
"""

clientes = ["Vanessa", "Ana Julia", "Pedro"]

for cliente in clientes:
    print(
        email_tmpl
        % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "escrever com tinta molhada",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )

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
print("\N{RED APPLE}")       # 🍎
print("\N{SMILING FACE}")    # 🙂
