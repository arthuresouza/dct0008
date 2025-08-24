"""
Exemplo de busca Linear e busca binária
"""

def buscaLinear(itemBusca, lista):
    for i in range(0,len(lista)):
        if lista[i] == itemBusca:
            return i
    return -1

def busaBinaria(itemBusca, lista):
    inicio = 0
    fim = len(lista)-1    
    while (inicio <= fim):
        meio = inicio+fim // 2
        if itemBusca < lista[meio]:
            fim = meio - 1
        elif itemBusca > lista[meio]:
            inicio = meio + 1
        else:
            return meio
    return -1
       


    

if __name__ == "__main__":
    lista = [1,2,3,4,4,5,6,7,7,8]
    lista2 = [1,2,3,4,4,5,6,1,7,8]
    #lista = [1,1,1,1,1]
    print(contarElemento(4,lista))
    print(ListarRepetidos(lista2))
    print(ListarRepetidos2(lista))