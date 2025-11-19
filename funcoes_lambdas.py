#Função lambda são anônimas e são passadas como argumento
#Função lambda só pode ter uma expressão (toda expressão retorna valor, por isso não precisa de return)

"""
def soma(a,b):
    retunr a+b

é a função lambda:
lambda a, b: a+b
"""

names = ["Bruno", "João", "Bernardo", "Cintia", "Marcia", "Juca"]
# ordenar os nomes que possuem letra "i"
print(sorted(names, key=lambda name: name.count("i")))

#listar os nomes que tem letra "b" em maiúsculo
print(list(filter(lambda name: name[0].lower()=="b", names)))

#listar Hello para cada nome da lista
print(list(map(lambda name: "Hello " + name, names)))

#############################################
#calculadora
operacao = input("Escolha a operação [sum, sub, mul, div]:").strip()
n1 = input("n1:").strip()
n2 = input("n2:").strip()

def soma(a,b):
    return a+b

operacoes = {
    "sum": soma, 
    "sub": lambda a,b: a-b, 
    "mul": lambda a,b: a*b, 
    "div": lambda a,b: a/b, 
}

resultado = operacoes[operacao](int(n1), int(n2))
print(f"O resultado é: {resultado}")