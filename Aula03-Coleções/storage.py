'''
Módulo para o armazenamento de dados de usuário em arquivo.
Autor: Arthur Souza auxiliado por Codepilot
'''

def salvarUsuario(usuario):
    ''' Função para salvar os dados do usuário em um arquivo texto. '''
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{usuario}\n")       


def lerUsuarios():
    ''' Função para ler todos os usuários cadastrados a partir do arquivo texto. '''
    usuarios = []
    with open("usuarios.txt", "rt") as arquivo:
        for linha in arquivo:
            nome, email, nascimento = linha.strip().split(",")
            usuarios.append({"nome": nome, "email": email, "nascimento": nascimento})
    return usuarios
