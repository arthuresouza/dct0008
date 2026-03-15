'''
Questão 11 - Soma o total dos elementos de uma lista.
'''

def somaTotal(lista):
    '''Soma o total dos elementos de uma lista.'''
    total = 0
    for elemento in lista:
        total += elemento
    return total

def somaTotalRange(lista):
    '''Soma o total dos elementos de uma lista com Range.'''
    total = 0
    for idx in range(len(lista)):
        total += lista[idx]
    return total

def somaTotalWhileIf(lista):
    '''Soma o total dos elementos de uma lista com While e If.'''
    total = 0
    idx = 0
    while True:
        if( idx >= len(lista)):
            break
        else:
            total += lista[idx]
        idx += 1
    return total

if __name__ == "__main__":
    minha_lista = [1, 2, 3, 4, 5]
    
    print(somaTotal(minha_lista))
    print(somaTotalRange(minha_lista))
    print(somaTotalWhileIf(minha_lista))