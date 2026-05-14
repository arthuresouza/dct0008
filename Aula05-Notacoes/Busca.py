"""
Exemplo de busca Linear e busca binária
"""

def buscaLinear(itemBusca, lista):
    for i in range(0,len(lista)):
        if lista[i] == itemBusca:
            return i
    return -1

def buscaBinaria(itemBusca, lista):
    inicio = 0
    fim = len(lista)-1    
    while (inicio <= fim):
        meio = (inicio+fim) // 2
        if itemBusca < lista[meio]:
            fim = meio - 1
        elif itemBusca > lista[meio]:
            inicio = meio + 1
        else:
            return meio
    return -1

def buscaBinariaLog(itemBusca, lista):
    inicio = 0
    fim = len(lista)-1
    espaco = 1    
    while (inicio <= fim):
        meio = (inicio+fim) // 2
        espaco *= 2
        print(f"Meio: {meio}, Inicio: {inicio}, Fim: {fim}, Espaço: n/{espaco} ")
        if itemBusca < lista[meio]:
            fim = meio - 1
        elif itemBusca > lista[meio]:
            inicio = meio + 1
        else:
            return meio
    return -1


if __name__ == "__main__":
    #lista = [1,2,3,4,4,5,6,7,7,8]
    #lista2 = range(1,100)
    #lista = [1,1,1,1,1]
    #print(buscaBinariaLog(99,lista2))
    #print(exponenciacao(10,1000))
    #print(exponenciacao_quadrados_expo_positivo(2,852))
    print(decimalBinario_01(14))