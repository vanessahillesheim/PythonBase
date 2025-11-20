#!/urs/bin/env python3

#EAFP - Easy to Ask Forgiveness than Permission
# É mais fácil perdir desculpas do que permissão = aqui põe para rodar e se tiver erro já tem o tratamento.
#No if/else, por exemplo, se verifica antes de fazer

"""
LBYL - Look before You Leap = Olhe antes de pular = if/else
EAFP = Mais fácil pedir desculpas que permissão = try/except

É necessário tratar os erros, para quando ocorrerem, não exibir ao usuário os dados do arquivo com erro. Ao usar o try/excep, corrigimos o problema dos erros exibidos no if/else, por exemplo.
usar try/except (ao invés de if/else) para tratamento de possíveis erros:
#except sozinho é um "Bare except" - qualquer erro q existir será capturado (em qualquer posição do arquivo) e vai  exibir a primeira mensagem de erro do arquivo. É melhor tratar as possibilidades de erros pontualmente:
- FileNotFounError
- ZeroDivisionError
- AttributeError
- ValueError
- RuntimeError
Dentro de um bloco try, eu posso ter todos os tipos de except para os erros acima.
No programa abaixo, "comentamos" os erros tratados e sua exibição de mensagem de [Error].
"""

import os
import sys
import logging

log = logging.Logger("erros")

def try_open_file(filepath, retry=1) -> list:
    #tente abrir o arquivo e tente novamente qtas vezes definidas no retry
    for attempt in range(1, retry +1):
        try:
            return open(filepath).readlines()
        except (FileNotFoundError, ZeroDivisionError) as e: #captura a mensagem de erro do FileNot Found e do ZeroDivision
           log.error("Erro: %s, e")
           time.sleep(2)
        else: #se não tiver except=erro, roda o else
            print("Sucesso!")
        finally: #independente de ter erro, vai executar
            print("Execute isso sempre!")
    return []

for line in try_open_file("names.txt", retry=5):
    print(line)
