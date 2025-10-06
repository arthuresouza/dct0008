"""
Aplicativo Agenda
"""

import Agenda

if __name__ == "__main__":
    contatos = Agenda.Contatos()
    opcao = int(input("1 - Salvar, 2-Listar, 3-Finalizar\n"))
    while opcao in [1,2]:
        if opcao == 1:
            nome = input("informe o nome: ")
            telefone = input("informe o telefone: ")
            email = input("informe o email: ")
            if input("Confirma inseção ? S-Sim, N-Não\n") == "S":
                contato = Agenda.Contato(nome,email,telefone)
                contatos.addContato(contato)
                contatos.salvarContatos()
        else:
            contatos = Agenda.Contatos()
            print(contatos.getAll())
        opcao = int(input("1 - Salvar, 2-Listar, 3-Finalizar: "))