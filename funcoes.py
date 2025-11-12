"""
#builtin
Funções embutidas no python: print, input, sum, open, max, min, len, reversed, sorted, filter, map, enumerate, zip

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
