# Código bugado
"""def repete_vogal(palavra):
    #retorna a palavra com as vogais repetidas.
    palavra_final = "" 
    for letra in palavra:
        if letra.lower() in "aeiouãõâôêéáíó":
            palavra_final = letra * 2
        else:
            palavra_final = letra
    return palavra_final

print(repete_vogal("banana"))"""


"""#utilizando o index e print para ver o que aconte em cada volta do loop
def repete_vogal(palavra):
    #retorna a palavra com as vogais repetidas.
    palavra_final = "" 
    for index, letra in enumerate(palavra):
        print(f"{index=} {letra=}")
        if letra.lower() in "aeiouãõâôêéáíó":
            palavra_final = letra * 2
        else:
            palavra_final = letra
        print(f"{palavra_final}")
    return palavra_final
print(repete_vogal("banana"))"""


"""#usando debug do Pyhton: no terminal digitar "python -m pdb", para verificar a execução passo a passo
def repete_vogal(palavra):
    #retorna a palavra com as vogais repetidas.
    palavra_final = "" 
    for letra in palavra:
        if letra.lower() in "aeiouãõâôêéáíó":
            palavra_final = letra * 2
        else:
            palavra_final = letra
        breakpoint()#parando a execução do programa neste ponto
    return palavra_final

print(repete_vogal("banana"))"""

#código corrigido
def repete_vogal(palavra):
    #retorna a palavra com as vogais repetidas.
    palavra_final = "" 
    for letra in palavra:
        if letra.lower() in "aeiouãõâôêéáíó":
            palavra_final += letra * 2
        else:
            palavra_final += letra
       
    return palavra_final

print(repete_vogal("banana"))