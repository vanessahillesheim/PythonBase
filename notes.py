#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotacao geral sobre carreira de tecnologia

$para executar o arquivo, digitar o comando "python notes.py new "minha 1ª nota""

...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"you must specify subcommand {cmds}")
    print("CLIQUE EM SHELL ACIMA E EXECUTE `python notes.py new teste")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

while True:
    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag?").strip().lower()
  
    # leitura das notas
        for line in open(filepath):
            title, tag, text = line.split("\t")
            if tag.lower() == arguments[1].lower():
                print(f"title: {title}")
                print(f"text: {text}")
                print("-" * 30)
                print()

    if arguments[0] == "new":
        try: 
            title = arguments[1]
        except IndexError:
            title = input("Qual o título?").strip().title()
        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:\n").strip(),
        ]
    # \t - tsv
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")

    continuar = input("Quer continuar? [N/y]").strip().lower()
    if continuar != "y":
        break
