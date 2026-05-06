"""
Algoritmo MergeSort
Adaptado do Livro Fundamentls of Python
"""


def mergeSortAux(lista, buffer, esquerda, direito, log=False):
    if(log):
        print(f'MergeSortAux => Esquerda: {esquerda}, Direita: {direito}, Lista: {lista[esquerda:direito+1]}')
    if esquerda < direito:
        meio = (esquerda + direito) // 2
        mergeSortAux(lista, buffer, esquerda, meio, log)
        mergeSortAux(lista, buffer, meio + 1, direito, log)
        merge(lista, buffer, esquerda, meio, direito, log)

def mergeSort(lista, log=False):
    # É necessário que a lista seja preenchida com elementos vazios
    # Para evitar o erro de indice inexistente
    buffer = [None] * len(lista) 
    mergeSortAux(lista, buffer, 0, len(lista) - 1, log)

def merge(lista, buffer, baixo, meio, alto, log=False):
    i1 = baixo
    i2 = meio + 1
    if(log):
        print(f' Merge => Lista1: {lista[baixo:meio+1]}, Lista2: {lista[meio+1:alto+1]}, Copia: {buffer}')  
        print(f' Merge => Esq: {baixo}, Dir: {alto}, Mei: {meio}')
    for i in range(baixo, alto + 1):
        if(log):
            print(f'i: {i}, i1: {i1}, i2: {i2}')
            print(f'buffer: {buffer}')
        if i1 > meio:
            buffer[i] = lista[i2]
            i2 += 1
        elif i2 > alto:
            buffer[i] = lista[i1]
            i1 += 1
        elif lista[i1] < lista[i2]:
            buffer[i] = lista[i1]
            i1 += 1
        else:
            buffer[i] = lista[i2]
            i2 += 1
    for i in range (baixo, alto + 1):
        lista[i] = buffer[i]

if __name__ == "__main__":
    lista = [3,2,8,1,5]
    mergeSort(lista, log=True)
    print(lista)

