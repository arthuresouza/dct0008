def insertionSort(lista):
    i = 1
    while i < len(lista):
        itemInserir = lista[i]
        j = i - 1
        while j >= 0:
            if itemInserir < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        lista[j + 1] = itemInserir
        i += 1

def insertionSortRec(lista, i=0):
    if(i == len(lista) - 1):
        return
    itemInserir = lista[i]
    j = i - 1
    while j >= 0:
        if itemInserir < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        else:
            break
    lista[j + 1] = itemInserir
    return insertionSortRec(lista,i+1)

def trocarPosicao(lista, indiceI, indiceJ):
    temp = lista[indiceJ]
    lista[indiceJ] = lista[indiceI]
    lista[indiceI] = temp

def selectionSort(lista):
    i = 0
    while i < len(lista) - 1:
        indicedoMenor = i
        j = i + 1
        while j < len(lista):
            if lista[j] < lista[indicedoMenor]:
                indicedoMenor = j
                j += 1
        if indicedoMenor != i:
            trocarPosicao(lista, indicedoMenor, i)
        i += 1
    return lista

def selectionSortRec(lista,i=0):
    if(i == len(lista) - 1):
        return lista
    indicedoMenor = i
    for j in range(i+1,len(lista)):
        if lista[j] < lista[indicedoMenor]:
            indicedoMenor = j
    if indicedoMenor != i:
        trocarPosicao(lista,indicedoMenor,i)
    return selectionSortRec(lista,i+1)    

def bubbleSort(lista):
    n = len(lista)
    while n > 1:
        i = 1
        while i < n:
            print(f'i: {i}, n: {n}')
            if lista[i] < lista[i - 1]:
                trocarPosicao(lista, i, i - 1)
            i += 1
        n -= 1
    return lista

def bubbleSortRec(lista, n=0):
    if n == 0: n = len(lista)
    if n <= 1:
        return lista
    else:
        i = 1
        while i < n:
            print(f'i: {i}, n: {n}')
            if lista[i] < lista[i - 1]:
                trocarPosicao(lista, i, i - 1)
            i += 1
        return bubbleSortRec(lista,n-1)

if __name__ == "__main__":
    lista = [3,2,8,2,5]
    print(bubbleSortRec(lista))