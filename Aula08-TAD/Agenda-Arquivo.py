ARQUIVO_AGENDA = "./Aula08-TAD/agenda.txt"

import ast

def salvaContato(nome, email, telefone):
       contato = {"nome": nome, "email": email, "telefone": telefone}
       with open(ARQUIVO_AGENDA,"a") as arquivo:
        arquivo.write(str(contato)+"\n") 
        arquivo.flush()
        arquivo.close()

def lerContatos():
    contatos = list()
    with open(ARQUIVO_AGENDA) as arquivo:
        for linha in arquivo:
            contatos.append(ast.literal_eval(linha.rstrip()))
        arquivo.close()
    return contatos    

if __name__ == "__main__":
    opcao = int(input("1 - Salvar, 2-Listar, 3-Finalizar\n"))
    while opcao in [1,2]:
        if opcao == 1:
            nome = input("informe o nome: ")
            telefone = input("informe o telefone: ")
            email = input("informe o email: ")
            if input("Confirma inseção ? S-Sim, N-Não\n") == "S":
                salvaContato(nome,email, telefone) 
        else:
            print(lerContatos())
        opcao = int(input("1 - Salvar, 2-Listar, 3-Finalizar"))
    

