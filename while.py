#!/usr/bin/env python3

#WHILE = enquanto a condição for verdadeira = repita!
# while opera em cima de uma condiçao (for opera em cima de uma coleção)

n = 0
while n < 101: #condição de parada
    print(n)
    n += 1

#utilizando BREAK para parar a execução
n1 = 0
while n1 <101:
    if n1 == 40:
        break # vai parar no 39
    print(n1)
    n1 +=1

#pulando o 40:
n2= 0
while n2<101:
    if n2 != 40:
        print(n2)
    n2 +=1

#pulando o 40 com, o CONTINUE
n3= 0
while n3<101:
    if n3 == 40:
        n3 += 1
        continue
    print(n3)
    n3 +=1

#pulando do 40 ao 60, com o CONTINUE
n4= 0
while n4<101:
    if n4 >= 40 and n4 <=60:
        n4 += 1
        continue
    print(n4)
    n4 +=1