nomes = ["Vanessa", 
         "Pedro", 
         "Ana Julia", 
         "Willian", 
         "Bernardo"
         ]

#função para listar texto q comença com letra "v" do objeto "nomes"
def comeca_com_v(texto):
    #return[0].lower()=="v"
    return texto.startswith(("v", "V"))

print(*list(filter(comeca_com_v, nomes)))

#estilo funcional = escrevendo a função no modo lambda 
print(*list(filter(lambda texto: texto[0].lower() == "b", nomes)), sep="\n")

#estilo procedural: listar texto q comença com letra "v" do objeto "nomes"
def comeca_com_w(texto):
    return texto[0].lower() == "w"

filtro = filter(comeca_com_w, nomes)
filtro = list(filtro)
for nome in filtro:
    print(nome)