"""
Algoritmo MergeSort 
Código do MergeSort comentado e com print de auxílio
Adaptado de https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html
"""
def mergeSort(lista):
    # Caso a lista tenha uma posição, está ordenada
    if len(lista) <= 1:
        return lista

    # Divide a lista ao meio
    meio = len(lista) // 2
    listaEsqueda = lista[:meio]
    listaDireita = lista[meio:]
    print(f'lista: {lista}, meio: {meio}, esqueda: {listaEsqueda}, direita: {listaDireita}')

    # Ordena as metades recursivamente
    listaEsqueda = mergeSort(listaEsqueda)
    listaDireita = mergeSort(listaDireita)

    # Combina as metades da lista
    return merge(listaEsqueda, listaDireita)

def merge(listaEsquerda, listaDireita):
    listaCombinada = []
    indiceEsquerdo = 0  # Indica o elemento da lista esquerda
    indiceDireito = 0  # Indica o elemento da lista direita

    print(f'Combinando esqueda: {listaEsquerda} + direita: {listaDireita}')
    log = ""
    # Compara os elementos das listas, selecionando o menor e incluindo na lista combinada
    while indiceEsquerdo < len(listaEsquerda) and indiceDireito < len(listaDireita):
        log += ""
        if listaEsquerda[indiceEsquerdo] < listaDireita[indiceDireito]:
            log += f"\tinsEsq {listaEsquerda[indiceEsquerdo]}"
            listaCombinada.append(listaEsquerda[indiceEsquerdo])
            indiceEsquerdo += 1
        else:
            log += f"\tinsDir {listaDireita[indiceDireito]}"
            listaCombinada.append(listaDireita[indiceDireito])
            indiceDireito += 1
    log += "\n"
    # Adiciona elementos restantes da lista esquerda
    while indiceEsquerdo < len(listaEsquerda):
        log += f"\tinsEsqRes {listaEsquerda[indiceEsquerdo]}"
        listaCombinada.append(listaEsquerda[indiceEsquerdo])
        indiceEsquerdo += 1

    # Adiciona elementos restantes da lista direita
    while indiceDireito < len(listaDireita):
        log += f"\tinsDirRes {listaDireita[indiceDireito]}"
        listaCombinada.append(listaDireita[indiceDireito])
        indiceDireito += 1

    log += "\n"
    print(f'{log}')
    print(f'Combinada: {listaCombinada}')
    return listaCombinada


if __name__ == "__main__":
    lista = [3,2,8,1,5]
    listaOrdenada = mergeSort(lista)
    print(f"Ordenada: {listaOrdenada}")