#!/urs/bin/env python3

#EAFP - Easy to Ask Forgiveness than Permission
# É mais fácil perdir desculpas do que permissão

"""
LBYL - Look before You Leap = Olhe antes de pular = if/else
EAFP = Mais fácil pedir desculpas que permissão = try/except

É necessário tratar os erros, para quando ocorrerem, não exibir ao usuário os dados do arquivo com erro. Ao usar o try/excep, corrigimos o problema dos erros exibidos no if/else, por exemplo.
usar try/except (ao invés de if/else) para tratamento de possíveis erros:
#except sozinho é um "Bare except" - qualquer erro q existir será capturado (em qualquer posição do arquivo) e vai  exibir a primeira mensagem de erro do arquivo. É melhor tratar as possibilidades de erros pontualmente:
- FileNotFounError
- ZeroDivisionError
- AttributeError
Dentro de um bloco try, eu posso ter todos os tipos de except para os erros acima.
No programa abaixo, "comentamos" os erros tratados e sua exibição de mensagem de [Error].
"""

import os
import sys

try:
    names = open("names.txt").readlines()
    #1 / 0 #ZeroDivisionError
    10 / 2
    #print(names.banana) #AttributeError
    print(names.append)
except FileNotFoundError:
    print("[Error] File names.txt not found.")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You can't divide by zero!")
    sys.exit(1)
except AttributeError:
    print("[Error] List doesn't have banana!")
    sys.exit(1)


try:
    print(names[2])
except:  #Bare except
    print("[Error] Missing name in the list.")
    sys.exit(1)