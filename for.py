#!/usr/bin/env python3


#FOR LOOPS = laço for
# for opera em cima de uma coleção (while opera em cima de uma condição)
"""
for n in [1,2,3]:
    print(n*2)

Quando se quer acumular dados, se utiliza uma lista vazia (começa vazia e ao executar o comando será preenchida)

dobrada = []
original = [1,2,3]

for n in original:
    dobrada.append(n*2)
print(dobrada)

#LIST COMPREHENSION (sempre cria uma lista nova) = ABORDAGEM FUNCIONAL 
original = [1,2,3]
dobrada = [n*2 for n in original]
print(dobrada)

#DICT COMPREHENSION
dados = {line for line in open("notes.txt")}
print(dados)

"""


#Quais os números pares de 1 a 110?
numbers = range(1,11)

#Iterable
for number in numbers:
    par = number %2 == 0
    if par:
        print(number)
    else: 
        continue 
    #Se o número não for par, ele vai para próxima linha
    #Se não colocar o continue, ele vai exibir a mensagem abaixo para nº ímpar tbém.
    print(f"Então: {number} é par!")

#para gerar a sequência de 1 a 10:
numeros = range(1,11)

#para imprimir números menores que 6

for numero in range(1, 11):
    if numero > 6:
        break
#para a execução
    if numero % 2 == 0:
        print(numero)
        print(f"Então, o número {numero} é par!")

#criando uma Dict comprehension utilizando os dados do arquivo notas_minha.txt
dados = {
    line.split(":")[0]:
    line.split(":")[1].strip()
    for line in open("notas_minha.txt")
    if ":" in line
    }
print(dados)

"""fazendo o mesmo dicionário, com for
dados1 = {}
for line in open("notas_minha.txt"):
    if ':' in line:
        key, valor = line.split(":")
        dados1[key] = valor.strip()
print(dados1)
"""     
 
   