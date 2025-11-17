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
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print(f"informe o nome do arquivo de e-mails.")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]
path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

with smtplib.SMTP(host="localhost", port=8025) as server:

    for line in open(filepath):
        nome, email = line.split(",")
        text =  (open(templatepath).read()
            % {
                "nome": nome,
                "produto": "caneta",
                "texto": "escrever com tinta molhada",
                "link": "https://canetaslegais.com",
                "quantidade": 1,
                "preco": 50.5,    
            } 
        )

        from_ = "vanessa@hillesheim.com"
        to = ",".join([email])
        message = MIMEText(text)
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to

        server.sendmail(from_, to, message.as_string())

        """
        Para executar:
        python -m aiosmtpd -n -l localhost:8025
        em outro terminal digitar: python .\interpolacao_smtp.py emails.txt email_tmpl.txt
        """