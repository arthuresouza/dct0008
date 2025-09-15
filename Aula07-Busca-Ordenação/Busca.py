def linear(lista, chave):
    """Retorna Verdadeiro se encontra o item na lista ou Falso se não encontra."""
    #Armazena a posição que está sendo verificada, inicia com 0
    posicaoVerificacao = 0
    #Compara a chave com os elmentos da posicao de verificação.
    while posicaoVerificacao < len(lista):
        if chave == lista[posicaoVerificacao]:
            return True
        posicaoVerificacao += 1
    return False

def linearRecursivo(lista, chave, posicao=0):
    if posicao == len(lista):
        return False    
    if chave == lista[posicao]:
        return True    
    linearRecursivo(lista,chave,posicao+1)

def binaria(listaOrdenada, chave):
    inicio = 0
    fim = len(listaOrdenada) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if chave == listaOrdenada[meio]:
            return True
        elif chave < listaOrdenada[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
        return False
    
def binariaRecursiva(listaOrdenada, chave):
    if len(listaOrdenada) == 1 and chave != listaOrdenada[0]:
        return False
    meio = len(listaOrdenada) // 2
    if chave == listaOrdenada[meio]: 
        return True
    elif chave < listaOrdenada[meio]:
        return binariaRecursiva(chave,listaOrdenada[:meio-1],)
    else:
        return binariaRecursiva(chave,listaOrdenada[meio+1:])