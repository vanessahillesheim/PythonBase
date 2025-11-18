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
