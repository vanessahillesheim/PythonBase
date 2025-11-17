"""
se der erro na execução: Ctrl+F5 ou
& C:/Users/admin/Desktop/Tecnologia/Python/PythonBase/venv/Scripts/python.exe c:/Users/admin/Desktop/Tecnologia/Python/PythonBase/funcoes.py


#builtin 
Funções embutidas (não precisam ser importadas) no python: print, input, sum, open, max, min, len, reversed, sorted, filter, map, enumerate, zip

#stdlib
Biblioteca que tem que ser importada da bliblioteca padrão

"""

numeros = [1,2,3,4,5]
print(sum(numeros))
#---------------------------------------------------------------------------------------
#REVERSED  = para inverter dados de uma lista
print(list(reversed(numeros)))

#---------------------------------------------------------------------------------------
#SORTED = para ordernar uma lista
num = [3,7,2,16,54,32]
print(sorted(num))

#---------------------------------------------------------------------------------------
##PROGRAMAÇÃO PROCEDURAL
#para filtrar números do texto
texto = "Vanessa154Hillesheim5484BR5465"
result = ""
for letra in texto:
    if letra.isdigit():
        result += letra
print(result)

##PROGRAMAÇÃO FUNCIONAL
#sempre retornará apenas o que for TRUE
#FILTER = para filtrar números do texto e exibir em formato de lista
text = "Vanessa154Hillesheim5484BR5465"
print(list(filter(str.isdigit, text)))

#FILTER = para filtrar números do texto e exibir em formato de texto
text = "Vanessa154Hillesheim5484BR5465"
print("".join(list(filter(str.isdigit, text)))) #começa vazio e vai juntando

#FILTER = para filtrar letras do texto e exibir em formato de texto
text = "Vanessa154Hillesheim5484BR5465"
print("".join(list(filter(str.isalpha, text)))) #começa vazio e vai juntando

#---------------------------------------------------------------------------------------
#MAP = se aplicado num objeto, sempre retorna o mesmo tipo de objeto (lista = lista; tupla = tupla)
nomes = ["Vanessa", "Hillesheim"]
resultado = [] 

##PROGRAMAÇÃO PROCEDURAL
# para colocar todas as letras maiúsculas
for nome in nomes:
    resultado.append(nome.upper())
print(resultado)

##PROGRAMAÇÃO FUNCIONAL
#mapeia a tuplas nomes e retorna uma tupla maiúscula
print(list(map(str.upper, nomes)))

dados = ([5,2,3,1,4], [1,2,3], [5,5,6])
print(dados)
len(dados)

#para somar os elementos de cada tupla do objeto "dados":
print(list(map(sum, dados)))

#para exibir o maior elemento dentro de cada tupla do objeto "dados":
print(list(map(max, dados)))

#para exibir o menor elemento dentro de cada tupla do objeto "dados":
print(list(map(min, dados)))

#---------------------------------------------------------------------------------------

names = ["Vanessa", "João", "Maria", "Miguel"]
#para imprimir a posição e o nome:
for name in names:
    print(names.index(name), name)

#se tiver nome repetido, a enumeração pelo index não funciona, porque ele retorna o primeiro que aparecer na lista:
names1 = ["Vanessa", "João", "Maria", "Vanessa", "Miguel"]
#para imprimir a posição e o nome:
for name1 in names1:
    print(names1.index(name1), name1)

#ENUMERATE para enumerar elementos:
for index, name1 in enumerate(names1):
    print(index, name1)

#ENUMERATE para enumerar elementos a partir de 5, por exemplo
for index, name1 in enumerate(names1, start=5):
    print(index, name1)

#---------------------------------------------------------------------------------------
#ZIP para juntar

colunas = ["nome", "sobrenome"]
dados1 = ["Vanessa", "Hillesheim"]
print(list(zip(colunas, dados1)))

#tornando dicionário
print(dict(zip(colunas, dados1)))

#acessando o primeiro valor do dicionario, pela chave "nome"
print(dict(zip(colunas, dados1))["nome"])

#---------------------------------------------------------------------------------------
#RANDOM
#para geração de número randômico

import random
print(random.random())

#para geração de número randômico inteiro, entre 1 e 11
print(random.randint(1,11))

#para fazer seleção aleatória a partir de uma coleção
cores = ["red", "green", "blue"]
print(random.choice(cores))

#para fazer seleção aleatória de 2 elementos, a partir de uma coleção
cores = ["red", "green", "blue"]
print(random.sample(cores,2))

#para embaralhar todos os elementos de uma coleção (mas sem alterar o objeto numbers)
numbers = [1,2,3,4,5,6,7]
print(random.sample(numbers,len(numbers)))
print(numbers)

#para embaralhar os elementos e ao mesmo tempo salvar essa nova posição do objeto (altera o objeto numbers) = alterção INPLACE
numbers1 = [1,2,3,4,5,6,7]
random.shuffle(numbers1)
print(numbers1)

#---------------------------------------------------------------------------------------
#ITERTOOLS: para manipular/gerar iteráveis

#Para trabalhar com objetos iteráveis
import itertools as it

#CYCLE = para repetir dados em ciclos indefinidos (só para com o break)
#usar para etiquetar itens, por exemplo (é um gerador de dados)

#para iterar a palavra Bruno com as letras do objeto ABCD, até o índice 10:
for index, item in enumerate(it.cycle("ABCD")):
    print(item, "Bruno")
    if index>10:
        break

#REPEAT = para repetir texto
#repetir "Bruno" 10x = gera uma lista
print(list(it.repeat("Bruno", 10)))

#ACUMULATE = para retornar os acumuladores da soma de dados de uma coleção (1+2=3, 3+3=6, 6+4=10, 10+5=15), então vai retornar: 1,3,6,10,15
numbers2 = [1,2,3,4,5]
print(list(it.accumulate(numbers2)))

#PRODUCT = para elevar a uma potência e exibir em lista. Neste caso vamos exibir a ABC de 2 em 2: AA, AB, AC, BA, BB, BC, CA, CB, CC
print(list(it.product("ABC",repeat=2)))

#PERMUTATIONS = para fazer permutação entre os elementos de um objeto (exibe uma lista com as variações de posições dos elementos do objeto): ABC, ACB, BAC, BCA, CAB, CBA
print(list(it.permutations("ABC")))

#COMBINATIONS = para combinar elementos, sem repetição (são únicas): red green, red blue e green blue
cores1 = ["red", "green", "blue"]
print(list(it.combinations(cores1,2)))

#---------------------------------------------------------------------------------------
#FUNCTOOLS: funções para manipular funções

import functools as ft

#PARTIAL = permite manipular parcialmente uma função do python
#Por exemplo, se quiser que imprima --- nos espaçoes entre as palavras:
#tradicional:
print("Vanessa", "Hillesheim", sep="---")

#customizando a função print
myprint= ft.partial(print, sep="---")
myprint("Vanessa", "Hillesheim")
#---------------------------------------------------------------------------------------

import statistics as st

numeros1 = [6,4,7,5,3,1,2]

#para saber a média de numeros1
print(st.mean(numeros1))

#para saber a mediana de numeros1
print(st.median(numeros1))

#---------------------------------------------------------------------------------------

import uuid

#para gerar idpython com chave hash aleatória: bb68341b-b969-4d5d-8c2a-306d7957d3ec
print(uuid.uuid4())

#---------------------------------------------------------------------------------------
import getpass

#serve para ler um input silencioso (o que o usuário digita não aparece, mas é salvo no BD)

first_name = input("Nome:")
password = getpass.getpass("Senha:")

