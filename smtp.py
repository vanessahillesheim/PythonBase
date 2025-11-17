#!/usr/bin/env python3

"""
Exemplos de envio de e-mail
"""

import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "vanessa@hillesheim.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu e-mail via Python"
#para evitar linhas em branco no início """\
TEXT = """\
Este é meu e-mail enviado via Python!
<b> Olá Mundo!</b>
"""

#mensagem formatada no formato SMTP
message = f"""
From: {FROM}
To: {TO}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))

#para rodar o programa:
#digitar: python -m aiosmtpd -n -l localhost:8025
#agora abrir outro terminal e digitar: python smtp.py