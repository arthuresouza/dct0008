'''
Modelando Usuário[nome,email,nascimento] com validação de email e data de nascimento.
Autor: Arthur Souza auxiliado por Codepilot
'''
import validation
from storage import salvarUsuario
from storage import lerUsuarios

def cadastrarUsuario():
    ''' Função para cadastrar um usuário, solicitando o nome e email. ''' 
    nome = input("informe o nome: ")
    email = lerEmail()    
    nascimento = lerDataNascimento()
    salvarUsuario({"nome": nome, "email": email, "nascimento": nascimento})        
    print(f"O usuário: {nome,email,nascimento} foi cadastrado com sucesso")

def lerEmail():
    ''' Função para ler um email válido do usuário. '''
    while True:
        email = input("informe o email (nome@email.com): ")
        if not validation.validarEmail(email):
            print("O email informado não é válido.\nExemplo de email válido: nome@dominio.com")
            continue
        break
    return email

def lerDataNascimento():
    ''' Função para ler uma data de nascimento válida do usuário. '''
    while True:
        data = input("informe a data de nascimento (dd/mm/aaaa): ")
        if not validation.validarDataNascimento(data):
            print("A data de nascimento informada não é válida.\nExemplo de data válida: 01/01/2000")
            continue
        break
    return data

def listarUsuarios():
    ''' Função para listar os usuários cadastrados. '''
    usuarios = lerUsuarios()
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return
    print("Usuários cadastrados:")
    for usuario in usuarios:
        print(usuario)

if __name__ == "__main__":
    '''Programa em módulos para cadastrar um usuário e listar os usuários cadastrados.'''
    print(">>>> Cadastro de Usuário <<<<")
    while True:
        print("0 - Finalizar\n1 - Cadastrar usuário\n2 - Listar usuários cadastrados")
        opcao = input("Escolha opção desejada: ")
        match opcao:
            case "0":
                print("Encerrando programa.")
                break
            case "1":
                cadastrarUsuario()
            case "2":
                listarUsuarios()
            case _:
                continue
