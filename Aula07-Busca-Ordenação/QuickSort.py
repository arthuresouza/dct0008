'''
Algoritmo QuickSort com Particionamento Lomuto
Adaptado do material em https://joaoarthurbm.github.io/eda/posts/quick-sort/
'''

def trocarPosicao(lista, indiceI, indiceJ):
    temp = lista[indiceJ]
    lista[indiceJ] = lista[indiceI]
    lista[indiceI] = temp

def particao(lista, esquerda, direita):
    pivot = lista[esquerda]
    fronteira = esquerda
    for i in range(esquerda,direita+1):
        if(lista[i] <= pivot):
            fronteira += 1
            trocarPosicao(lista,i,fronteira)
    trocarPosicao(lista,esquerda,fronteira)

def quickSort(lista,esquerda,direita):
    if(esquerda < direita):
        indexPivot = particao(lista,esquerda,direita)
        quickSort(lista,esquerda, indexPivot - 1)
        quickSort(lista,indexPivot+1,direita)