def binariaRecursiva(itemBusca, lista):
    if len(lista) == 1 and itemBusca != lista[0]:
        return False
    meio = len(lista) // 2
    print(f'meio {meio}, lista: {lista}')
    if itemBusca == lista[meio]: 
        return True
    elif itemBusca < lista[meio]:
        return binariaRecursiva(itemBusca,lista[:meio-1],)
    else:
        return binariaRecursiva(itemBusca,lista[meio+1:])
    
if __name__ == "__main__":
    #lista = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    lista = [2, 5, 8, 12, 16]
    print(binariaRecursiva(2,lista))