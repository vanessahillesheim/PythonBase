#!/usr/bin/env python3

"""Cadastro do Produto"""
__version__ ="0.1.0"

produto = {
    "nome": "caneta", 
    "cores": ["azul","branco"], 
    "preco" : 3.23,
    "dimensao": {"altura": 12.1, "largura" : 0.8}, 
    "em_estoque": True, 
    "codigo": 45678, 
    "codebar": None
}

cliente = {
    "nome": "Vanessa"
}

compra = {
    "cliente": cliente, 
    "produto": produto,
    "qtdade": 3}

total_compra = compra["qtdade"] * compra["produto"]["preco"]

print(f"O(a) cliente {compra['cliente']['nome']} comprou {compra['qtdade']} {compra['produto']['nome']}(s) "
      f"e pagou o total de R${total_compra:.2f}.")

