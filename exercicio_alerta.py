"""
Faça um script que pergunta ao usuário qual a temperatura atual e o índice de umidade do ar, sendo que será exibida mensagem de alerta para as condições:

temp maior 45: ALERTA!!! Perido: calor extremo!
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perido: calor úmido!
temp entre 10 e 30: Normal!
temp entre 0 e 10: Frio!
temp <0: ALERTA!!! Frio extremo"
"""

"""
temp = float(input('Qual a temperatura atual?'))
umid = float(input('Qual a taxa de umidade do ar?'))

if temp >45 and temp*3 <= umid:
    print(f"ALERTA! Perigo: calor úmido!")
elif temp >= 45:
    print(f"ALERTA! Perigo: calor extremo!")
elif temp > 30 and temp <45: 
    print(f"Calor!")
elif temp > 10 and temp <=30: 
    print(f"Normal!")
elif temp > 0 and temp <=10: 
    print(f"Frio!")
elif temp <0:
    print(f"Frio extremo!")

"""
#Resolução do professor:

import sys
import logging
log = logging.Logger("alerta")

def dicionario_preenchido(dicionario_inputs):
    info_size = len(dicionario_inputs)
    filled_size = len([value for value in dicionario_inputs.values() if value is not None])
    return info_size == filled_size

def leia_inputs_dicionario(dicionario_inputs):
    for key in dicionario_inputs.keys():
            if dicionario_inputs[key] is not None:
                continue
            try:
                dicionario_inputs[key]= float(input(f"Qual a {key} atual?").strip())
            except ValueError:
                log.error("%s inválida. Digite números!", key)
             
#PROGRAMA PRINCIPAL

info = {
    "temperatura": None, 
    "umidade": None
}

while not dicionario_preenchido(info):
    leia_inputs_dicionario(info)  
    
temp, umid = info.values()

if temp >45:
    print(f"ALERTA! Perigo: calor extremo!")
elif temp>30 and temp *3>= umid:
    print(f"ALERTA! Perigo: calor úmido!")
elif temp > 10 and temp <=30: 
    print(f"Normal!")
elif temp >= 0 and temp <=10: 
    print(f"Frio!")
elif temp <0:
    print(f"Frio extremo!")




