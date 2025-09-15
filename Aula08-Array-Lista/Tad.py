def variaveis():
    nome = "Arthur Souza"
    endereco = "Rua Serra da Saudade"
    numero = 2443

def salvaNomes(nomes):
    with open("./Aula08-Array-Lista/lista_nomes.txt","a") as arquivo:
        for nome in nomes:
            arquivo.write(nome+"\n") 
        arquivo.flush()
        arquivo.close()
    print(nomes)

def lerNomes():
    nomes = list()
    with open("./Aula08-Array-Lista/lista_nomes.txt") as fil:
        for linha in fil:
            nomes.append(linha.rsplit())
        fil.close()
    print(nomes)

if __name__ == "__main__":
    lerNomes()