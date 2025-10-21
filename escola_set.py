#!/usr/bin/env python3

"""
Exibir relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala, que frequentam cada uma das atividades.
Para ativar o ambiente virtual: venv\Scripts\Activate.ps1
"""
__version__ ="0.1.1"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Ester"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

#aqui temos tuplas com label:
atividades = [("Inglês", aula_ingles), 
              ("Música", aula_musica), 
              ("Dança", aula_danca)]
# na 1ª volta do loop, vai exibir os alunos da aula de ingês, no 2º aula de música e no 3º aula de dança


#Listar alunos em cada atividade por sala
for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}:\n")


#sala1 que tem intersecção com a atividade
    atividade_sala1 = set(sala1)&set(atividade)
    atividade_sala2 = set(sala2)&set(atividade)


    print(f" sala1 ", atividade_sala1)
    print(f" sala2 ", atividade_sala2)
    print("_"*40)