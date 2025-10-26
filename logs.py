#!/usr/bin/env python3

import logging
import os
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()


#Instância de logging
log = logging.Logger("Vanessa", log_level)

#Level

#Handler - destino da msg de logging com erro
#ch = logging.StreamHandler() #por padrão, exibe na tela/terminal
#ch.setLevel(log_level)

#Handler - destino da msg de logging, será um arquivo externo
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=300, #10**6
    backupCount=10
)
fh.setLevel(log_level)

#Formatação
fmt = logging.Formatter('%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s')
#ch.setFormatter(fmt)
fh.setFormatter(fmt)

#destino
#log.addHandler(ch)
log.addHandler(fh)

log.debug("Mensagem para desenvolvedor, qe, administrador")
log.info("Mensagem para usuários.")
log.warning("Aviso que não causa erro.")
log.error("Erro que afeta uma única execução.")
log.critical("Erro geral. Ex: BD sumiu!")

print("----")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("Deu erro %s", str(e))