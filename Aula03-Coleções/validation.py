'''
Módulo para validação de dados do usuário.
Autor: Arthur Souza auxiliado por Codepilot
'''

def validarEmail(email):
    ''' Função para validar o formato do email. '''
    if "@" in email and "." in email:
        indexArroba = 0
        indexPonto = 0
        for i in range(len(email)):
            if email[i] == "@":
                indexArroba = i
            elif email[i] == ".":
                indexPonto = i
        if indexArroba < indexPonto:
            return True
    return False

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