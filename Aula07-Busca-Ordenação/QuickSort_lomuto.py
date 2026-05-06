'''
Algoritmo QuickSort com Particionamento do Pivot no Meio
Adaptado do material em Fundamentals of Python Data Structures, Kenneth A. Lambert, 2011
'''

def trocarPosicao(lista, indiceI, indiceJ):
    temp = lista[indiceJ]
    lista[indiceJ] = lista[indiceI]
    lista[indiceI] = temp

def particao(lista, esquerda, direita):
    meio = (esquerda + direita) // 2 
    pivot = lista[meio]
    trocarPosicao(lista, meio, direita)
    fronteira = esquerda
    for index in range(esquerda,direita):
        if(lista[index] < pivot):
            trocarPosicao(lista,index,fronteira)
            fronteira += 1            
    trocarPosicao(lista,direita,fronteira)
    return fronteira

def quickSortAux(lista,esquerda,direita):
    if(esquerda < direita):
        indexPivot = particao(lista,esquerda,direita)
        quickSortAux(lista,esquerda, indexPivot - 1)
        quickSortAux(lista,indexPivot+1,direita)

def quickSort(lista, log=False):
    if log:
        quickSortAuxLog(lista,0,len(lista)-1,1)
    else:
        quickSortAux(lista,0,len(lista)-1)

def quickSortAuxLog(lista,esquerda,direita,particoes):
    
    if(esquerda < direita):
        indexPivot = particao(lista,esquerda,direita)
        print(f"Partição {particoes}: {lista[esquerda:direita+1]} com pivot {lista[indexPivot]}, índice {indexPivot}")
        quickSortAuxLog(lista,esquerda, indexPivot - 1,particoes+1)
        quickSortAuxLog(lista,indexPivot+1,direita,particoes+1)

if __name__ == "__main__":
    lista = [3,2,8,1,5]
    quickSort(lista, log=True)
    print("Lista ordenada:", lista)  