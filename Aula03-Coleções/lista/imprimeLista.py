'''
Questão 10 - Imprima os elementos de uma lista.
'''

def imprimeLista(lista):
    '''Imprime os elementos de uma lista.'''
    for elemento in lista:
        print(elemento)

def imprimeListaRange(lista):
    '''Imprime os elementos de uma lista com Range.'''
    for idx in range(len(lista)):
        print(lista[idx])

def imprimeListaWhile(lista):
    '''Imprime os elementos de uma lista com While.'''
    idx = 0
    while idx < len(lista):
        print(lista[idx])
        idx += 1

if __name__ == "__main__":
    minha_lista = [1, 2, 3, 4, 5]
    
    imprimeLista(minha_lista)
    imprimeListaRange(minha_lista)
    imprimeListaWhile(minha_lista)