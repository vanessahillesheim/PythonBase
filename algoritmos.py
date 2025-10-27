#!/usr/bin/env python3

""" 
ALGORITMOS: são instruções lógicas e organizadas que servem para resolver um problema ou executar uma tarefa.

A padaria está aberta?
Se é feriado e NÃO é natal: não
Senão, Se é sábado OU domingo E antes do meio dia: sim
Senão, se é dia de semana E antes das 19h: sim
senão: não
Se padaria está aberta E:
Se está chovendo: Pegar guarda-chuvas
Se está chovendo E calor: Pegar guarda-chuvas e garrafa de agua
Se está chovendo E frio OU nevando: pegar guarda chuva, blusa e botas
Ir até a padaria:
Se tem pao integral E baguete: Pedir 6 de cada
Senão, se tem apenas pao integral OU baguete: Pedir 12
Senão: Pedir 6 de qualquer pão
Senão
Ficar em casa em comer bolachas

# STATEMENTES -> são declarações/instrução/ordem para o computador executar
-Se -> if
-Senão, se-> elif
-Senão -> else

# OPERADORES LÓGICOS
-E -> and
-Ou -> or
-Não -> not

# ASSIGNMENTS -> ATRIBUIÇÃO é o ato de guardar um valor em uma variável.
- A padaria está aberta? true ou false

# EXPRESSIONS -> é a combinação de valores, variáveis e operadores, que produzem resultado.
Toda vez que eu esperar uma resposta, é uma expressão.
é feriado? -> boll = true/false
é Natal? -> true/false
é feriado e NÃO é Natal? true/false
é sábado? true/false
é domingo? true/false
é sábado OU domingo? true/false

# ACTIONS -> são funções, métodos e instruções
"""
__version__ = "0.1.1"
__author__ = "Vanessa Hillesheim"


#PSEUDO CÓDIGO
import ir, pegar, pedir, tem, comer, ficar #importamos as funções disponibilizadas no Python

today = "Segunda"
hora = 15
natal = False
chovendo = True
frio = True
nevando = True
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
feriado = ["Quarta"]
horario_padaria = {
    "semana" = 19,
    "findi" = 12
}

#algoritmo

#validação: padaria está ou não aberta?
if today in feriado and not natal:
    padaria_aberta = False
elif today not in semana and hora <horario_padaria["findi"]:
    padaria_aberta = True
elif today in semana and hora <horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False

#padaria aberta e:
if padaria_aberta is True:
    if chovendo and (frio or nevando):
        pegar("guarda-chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda-chuvas")
        pegar("água")
    elif chovendo:
        pegar("guarda-chuvas")

#padaria aberta e preparada para sair. Agora ir para padaria
    ir("padaria")

#o que comprar na padaria
    if tem("pão integral") and tem("baguete"):
        pedir(6, "pão integral")
        pedir(6, "baguete")
    elif tem("pão integral") or tem("baguete"):
        pedir(12, "qualquer um dos 2" )
    else: 
        pedir(6, "qualquer pão")

#se padaria fechada:
else:
    ficar("casa")
    comer("bolacha")

        
    

