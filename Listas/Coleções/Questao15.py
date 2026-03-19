'''
Questão 15. Escreva uma função Python removerInicio(dicionario) que recebe um dicionário
no formato: {“1o”: “um”, “2o”: “dois”, “3o”: “três”, …},
remove o primeiro elemento, desloca os outros para posições anteriores
e imprime o resultado.
Por exemplo, ao executarmos uma vez teremos o resultado: 
{“1o”: “dois”, “2o”: “três”, “3o”: “quatro”, …} 

Autor: Arthur Souza auxiliado por Codepilot
'''

def removerInicio(dicionario):
    ''' Função para remover o primeiro elemento de um dicionário e deslocar os outros.
        Lógica: crie uma variável de controle para iterar sobre as chaves do dicionário,
        e para cada chave, atribua o valor da próxima chave.
        Para a última chave, atribua uma string vazia.'''
    chavesDicionario = list(dicionario.keys())
    idx = 1
    for chave in chavesDicionario:
        if idx < len(chavesDicionario):
            dicionario[chave] = dicionario[chavesDicionario[idx]]
        else:
            dicionario[chave] = ""
        idx += 1
    return dicionario 


if __name__ == "__main__":
    dicionario = {"1o": "um", "2o": "dois", "3o": "três", "4o": "quatro"}
    print("Dicionário original:", dicionario)
    resultado = removerInicio(dicionario)
    print("Dicionário após remover o primeiro elemento:", resultado)