"""
Faça um programa que pede ao usuári que digite uma ou mais palavras e imprima cada uma das palavras com as suas vogais duplicadas:

Exemplo:
'Digite uma palavra (ou enter para sair): 'Vanessa'
Vaaneessaa
"""

import sys
import logging
log = logging.Logger("alerta")

# Lista de vogais (incluindo acentuadas)
vogais = ["a","e","i","o","u","A","E","I","O","U","á","Á","ã","Ã","â","Â","ê","Ê","í","Í","õ","Õ","ó","Ó","ô","Ô","ú","Ú"]

while True:
    try:
        palavra = input("Digite uma palavra que iremos duplicar as vogais (ou enter para sair): ").strip()
        
        # Se usuário digitar enter, sai do programa
        if palavra == "":
            print("Saindo...")
            break
            
        # Validação se contém apenas letras
        if not palavra.replace(" ", "").isalpha():
            raise ValueError("Digite apenas letras!")
        
        # Duplica as vogais
        resultado = ""
        for letra in palavra:
            if letra in vogais:
                resultado += letra * 2  # Duplica a vogal
            else:
                resultado += letra  # Mantém a consoante
        
        print(f"Resultado: {resultado}")
        
    except ValueError as e:
        print(f"Erro: {e}")

"""
#Resolução do professor:

words = []
while True:
    word = input("Digite uma palavra (ou enter para sair):").strip()
    if not word:
        break
   
   
    final_word = "" #palavra final começa fazia

    for letter in word:
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)

for word in words:
    print(word)

"""