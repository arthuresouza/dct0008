'''
Modelando Usuário como nome e email com dados básicos.
Autor: Arthur Souza
'''

def cadastrarUsuario():
    ''' Função para cadastrar um usuário, solicitando o nome e email. ''' 
    nome = input("informe o nome: ")
    email = input("informe o email: ")
    print("O usuário foi cadastrado com sucesso")

if __name__ == "__main__":
    cadastrarUsuario()