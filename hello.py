#!usr/binn/env python3
"""
Dependendo da língua configurada no ambiente, o programa exibe a mensagem correspondente.
Obs: necessário criar um ambiente virtual (python -m venv venv), para rodar em qualquer máquina.
Para ativar o ambiente virtual: venv\Scripts\Activate.ps1


Como usar:
Tenha a variável LANG devidamente configurada. Por exemplo:
    export LANG=pt_BR

Execução (digitar no terminal):
python hello.py
ou
./hello.py

"""
__version__ = "0.0.1"
__author__ = "Vanessa Hillesheim"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello world!"

if current_language == "pt_BR":
    msg = "Olá mundo!"
elif current_language == "it_IT":
    msg = "Ciao mondo!"
elif current_language == "es_SP":
    msg = "Hola mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour monde!"
