"""
Conta elementos de uma lista
"""

def contarElemento(itemBusca, lista):
    contador = 0
    for item in lista:
        if item == itemBusca:
            contador += 1
    return contador

def ListarRepetidos(lista):
    repetidos = set()
    for i in range(0,len(lista)):
        for j in range(0,len(lista)):
            if i != j and (lista[i] == lista[j]):
                repetidos.add(lista[i])        
    return repetidos

def ListarRepetidos1(lista):
    repetidos = set()
    for i in range(0,len(lista)):
        for j in range(i+1,len(lista)):
            if (lista[i] == lista[j]):
                repetidos.add(lista[i])        
    return repetidos

def ListarRepetidos2(lista):
    repetidos = set()
    visitados = set()
    for i in lista:
        if i in visitados:
            repetidos.add(i)
        else:
            visitados.add(i)
    return repetidos

    

if __name__ == "__main__":
    lista = [1,2,3,4,4,5,6,7,7,8]
    lista2 = [1,2,3,4,4,5,6,1,7,8]
    #lista = [1,1,1,1,1]
    print(contarElemento(4,lista))
    print(ListarRepetidos(lista2))
    print(ListarRepetidos2(lista))