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

info = {
    "temperatura": None, 
    "umidade": None
}

while True:
    #condição de parada
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])
      
    if info_size == filled_size:
        break


    for key in info.keys():
        if info[key] is not None:
            continue
        try:
            info[key]= float(input(f"Qual a {key} atual?").strip())
        except ValueError:
            log.error("%s inválida. Digite números!", key)
            break

temp, umid = info.values()

if temp >45 and temp*3 >= umid:
    print(f"ALERTA! Perigo: calor extremo!")
elif temp>= 45:
    print(f"ALERTA! Perigo: calor úmido!")
elif temp > 10 and temp <=30: 
    print(f"Normal!")
elif temp >= 0 and temp <=10: 
    print(f"Frio!")
elif temp <0:
    print(f"Frio extremo!")




