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

def nome_da_funcao(a: int, b: int, c: int)->int:
    """
    use esta função para saber a soma de a+b+c;
    quando o parâmetro "a" tiver o valor 10, vai acontecer X...
    
    >>>nome_da_funcao(1,2,3)
    6    
    """    
    resultado = a+b+c
    return resultado
print(nome_da_funcao(1,2,3))

#no terminal, se quiser ver a ajuda da função, digito: help(nome_da_funcao)
