"""
Algoritmo MergeSort
Adaptado do Livro Fundamentls of Python
"""
def mergeSortAux(lista, buffer, esquerda, direito):
    print(f'Aux =>Esq: {esquerda}, Dir: {direito}, copia: {buffer}')
    if esquerda < direito:
        meio = (esquerda + direito) // 2
        mergeSortAux(lista, buffer, esquerda, meio)
        mergeSortAux(lista, buffer, meio + 1, direito)
        merge(lista, buffer, esquerda, meio, direito)

def mergeSort(lista):
    # É necessário que a lista seja preenchida com elementos vazios
    # Para evitar o erro de indice inexistente
    buffer = [None] * len(lista) 
    mergeSortAux(lista, buffer, 0, len(lista) - 1)

def merge(lista, buffer, baixo, meio, alto):
    print(f' Merge => Lista: {lista}, Copia: {buffer}')
    i1 = baixo
    i2 = meio + 1
    print(f' Merge => Esq: {baixo}, Dir: {alto}, Mei: {meio}')
    for i in range(baixo, alto + 1):
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
    mergeSort(lista)
    print(lista)

