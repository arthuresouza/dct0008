def contarCaracteres(string:str):
    caracteres = 0 # 1
    numeros = 0 # 1
    pontuacoes = 0 # 1
    for i in string: # n
        if(i.isalpha()): # 1 .. n
            caracteres += 1 # 0 .. n
        elif(i.isnumeric()): # 0 .. n
            numeros += 1 # 0 .. n
        else: # 0 .. n
            pontuacoes +=1 # 0 .. n
    return f'Letras: {caracteres}, Números: {numeros}, Pontuações: {pontuacoes}' # 1

if __name__ == "__main__":
    texto = "Texto exemplo 01."
    print(contarCaracteres(texto))