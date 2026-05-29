'''
Algoritmo QuickSort com Pivot do Primeiro Elemento, parcionamento Lomuto
Adaptado do material em https://joaoarthurbm.github.io/eda/posts/quick-sort/
'''

def trocarPosicao(lista, indiceI, indiceJ):
    temp = lista[indiceJ]
    lista[indiceJ] = lista[indiceI]
    lista[indiceI] = temp

def particao(lista, esquerda, direita, log=False):
    pivot = lista[esquerda]
    fronteira = esquerda
    if(log):
            print(f'Pivot: {pivot}, Lista-Antes-Particao: {lista[esquerda:direita+1]}, Fronteira: {fronteira}')
    for i in range(esquerda+1,direita+1):
        if(lista[i] <= pivot):
            fronteira += 1
            trocarPosicao(lista,i,fronteira)
        if(log):
            print(f'I: {i}, Lista: {lista[esquerda:direita+1]}, Fronteira: {fronteira}')        
    trocarPosicao(lista,esquerda,fronteira)
    if(log):
            print(f'Pivot: {pivot}, Lista-Depois-Particao: {lista[esquerda:direita+1]}, Fronteira: {fronteira}')
    return fronteira

def quickSort(lista,esquerda,direita, log=False):
    if(esquerda < direita):
        indexPivot = particao(lista,esquerda,direita, log)
        quickSort(lista,esquerda, indexPivot - 1, log)
        quickSort(lista,indexPivot+1,direita, log)

if __name__ == "__main__":
    #lista = [3,2,8,1,5]
    lista = [3,2,8,1,5]
    n = len(lista)
    print("Lista original:", lista)
    quickSort(lista, 0, n-1, log=True)
    print("Lista ordenada:", lista)  