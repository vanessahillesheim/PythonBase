"""
## Anatomia antiga da função
#definição ou atribuição = nome da função
def nome_da_funcao

#assinatura da função = tudo o que estiver no parenteses
(a,b,c)
def nome_da_funcao(a,b,c):

#documentação/docstring
#numa sentença, expressar o que a função faz

def nome_da_funcao(a,b,c):
    use esta função para saber a soma de a+b+c;
    quando o parâmetro "a" tiver o valor 10, vai acontecer X...
    :param a: número inteiro
    :type a: int
    :param b: número inteiro
    :type b: int
    :param c: número inteiro
    :type c: int
    :return: retorna o resultado de a+b+c
    :type return: int
 """   

##Anatomia atualizada da função - elementos da função
#definição ou atribuição = nome da função
#assinatura da função = tudo o que estiver no parenteses + tipo da variável
#documentação/docstring
#código
#valor de retorno
#para executar este arquivo: %run funcoes_anatomia.py e help(nome_da_funcao)


def nome_da_funcao(a: int, b: int, c: int)->int:
    """
    use esta função para saber a soma de a+b+c;
    quando o parâmetro "a" tiver o valor 10, vai acontecer X...
    
    >>>nome_da_funcao(1,2,3)
    6    
    """    
    resultado = a+b+c
    return resultado

#passagem de argumentos posicionais
valor = nome_da_funcao(1,2,3)
print(valor)

#passagem de argumentos nomeados
valor = nome_da_funcao(a=2,b=3,c=1)
print(valor)

#passagem mista de argumentos
#argumentos posicionais devem vir antes dos argumentos nomeados
valor = nome_da_funcao(1, c=3, b=2)
print(valor)

#######################################################################

def outra_funcao(a,b,c):
    """Explicar o q a função faz"""
    return a*2, b*2, c*2

outro_valor = outra_funcao(1,2,3)
print(outro_valor) #retorna uma tupla e guarda em uma única variável

valor1, valor2, valor3 = outra_funcao(1,2,3) #retorna 3 valores e guarda em 3 variáveis
print(valor1)
print(valor2)
print(valor3)

valor4, *resto = outra_funcao(1,2,3) #retorna o valor 4 sepado do resto e guarda em 2 variáveis
print(valor4)
print(resto)

#######################################################################

# Passagem de argumentos com desempacotamento

def soma(n1, n2):
    """Faz a soma de 2 números"""
    return n1+n2

#normal
print(soma(10,20))

#argumentos em sequência/posicional
args = (20,30) #tupla
print(soma(args[0], args[1]))
print(soma(*args)) #maneira diferente de imprimir a mesma coisa (*para lista)

#argumentos dicionário/nomeados
args = {"n2": 90, "n1": 100}
print(soma(n1=args["n1"], n2=args["n2"]))
print(soma(**args)) #maneira diferente de imprimir a mesma coisa (**para dicionário)

lista_de_valores_para_somar = [
    {"n2": 90, "n1": 100}, 
    {"n2": 90, "n1": 200}, 
    {"n2": 9, "n1": 650}, 
    (5,10), 
    [8,13]
]

for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print(soma(**item)) #se for dicionário **; se for lista/tupla *
    else:
        print(soma(*item))