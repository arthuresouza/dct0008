'''
Algoritmo QuickSort com Pivot do Primeiro Elemento
Adaptado do material em https://joaoarthurbm.github.io/eda/posts/quick-sort/
'''

def trocarPosicao(lista, indiceI, indiceJ):
    temp = lista[indiceJ]
    lista[indiceJ] = lista[indiceI]
    lista[indiceI] = temp

def particao(lista, esquerda, direita):
    pivot = lista[esquerda]
    fronteira = esquerda
    for i in range(esquerda+1,direita+1):
        if(lista[i] <= pivot):
            fronteira += 1
            trocarPosicao(lista,i,fronteira)
    trocarPosicao(lista,esquerda,fronteira)
    return fronteira

def quickSort(lista,esquerda,direita):
    if(esquerda < direita):
        indexPivot = particao(lista,esquerda,direita)
        quickSort(lista,esquerda, indexPivot - 1)
        quickSort(lista,indexPivot+1,direita)

if __name__ == "__main__":
    #lista = [3,2,8,1,5]
    lista = [3,2,8,1,5]
    n = len(lista)
    print("Lista original:", lista)
    quickSort(lista, 0, n-1)
    print("Lista ordenada:", lista)  