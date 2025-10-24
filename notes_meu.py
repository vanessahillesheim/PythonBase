#!usr/bin/env python3

"""
BLOCO DE NOTAS

$notes.py new "minha nota"
tag: input para descrição
text: input para descrição
Exemplo: anotações gerais sobre carreira de tecnologia.

Uso:
Os registros das anotações devem ser armazendos num arquivo txt
"""

__version__ = "0.1.1"
__author__ = "Vanessa"

import sys
import os
#para gravar a data e local do login
from datetime import datetime


argumentos = sys.argv[1:]

if not argumentos:
    titulo = input(f"Digite o título da nota:")
    tag = input(f"Digite a tag:")
    text = input(f"Descreva a anotação:")
elif len(argumentos) == 3:
    # Se foram passados 3 argumentos via linha de comando
    titulo, tag, text = argumentos
else:
    print("Preencha o título, tag e faça sua anotação!")
    print("Uso: python notes.py [titulo tag texto]")
    sys.exit(1)

#para gravar as notações no arquivo notas.txt com o log do usuario/dia/hora
path = os.curdir
filepath = os.path.join(path, "notas_minha.txt")
timestamp = datetime.now().isoformat()
usuario = os.getenv('USER', 'anonymous')

with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {usuario}\nTítulo: {titulo}\nTag: {tag}\nTexto: {text}\n\n")
    print(f"Nota salva com sucesso em {filepath}!")