"""
print("Welcome to the test!")
input("When you are ready, press Enter.")

name = input("name:")
print(f"It's nice to meet you {name}")

color = input("What is your favorite color?")
print(f"{color} is a great color!")

input("Describe yourself:")
print("Admirable!")

print("Goodbye!")
"""
#usando funções para organizar o código

def welcome():
    print("Welcome to the test!")
    input("When you are ready, press Enter.")

def ask_questions():
    name = input("name:")
    print(f"It's nice to meet you {name}")

    color = input("What is your favorite color?")
    print(f"{color} is a great color!")

    input("Describe yourself:")
    print("Admirable!")

def goodbye():
    print("Goodbye!")

#determinando a execução das funções:
welcome()
ask_questions()
goodbye()

