'''
Modelando Usuário[nome,email,nascimento] com validação de email e data de nascimento.
Autor: Arthur Souza auxiliado por Codepilot
'''

def validarEmail(email):
    ''' Função para validar o formato do email. '''
    if "@" in email and "." in email:
        return True
    return False

def lerEmail():
    ''' Função para ler um email válido do usuário. '''
    while True:
        email = input("informe o email (nome@email.com): ")
        if not validarEmail(email):
            print("O email informado não é válido.\nExemplo de email válido: nome@dominio.com")
            continue
        break
    return email

def validarDataNascimento(data):
    ''' Função para validar o formato da data de nascimento. '''
    ''' Valida o formato '''
    if len(data) != 10: return False
    if data[2] != '/' or data[5] != '/': return False
    ''' Valida os valores '''
    dia = data[0:2]
    mes = data[3:5]
    ano = data[6:10]
    if dia.isnumeric() and mes.isnumeric() and ano.isnumeric():
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        if (1 <= dia <= 31 and 1 <= mes <= 12 and ano > 1900):
            return True
    return False

def lerDataNascimento():
    ''' Função para ler uma data de nascimento válida do usuário. '''
    while True:
        data = input("informe a data de nascimento (dd/mm/aaaa): ")
        if not validarDataNascimento(data):
            print("A data de nascimento informada não é válida.\nExemplo de data válida: 01/01/2000")
            continue
        break
    return data

def cadastrarUsuario():
    ''' Função para cadastrar um usuário, solicitando o nome e email. ''' 
    nome = input("informe o nome: ")
    email = lerEmail()    
    nascimento = lerDataNascimento()        
    print(f"O usuário: {nome,email,nascimento} foi cadastrado com sucesso")

if __name__ == "__main__":
    cadastrarUsuario()