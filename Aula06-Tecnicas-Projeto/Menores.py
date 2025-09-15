#Busca Linear
def linearMenor(lista:list):
    menor = lista[0]
    for i in range(1,len(lista)):
        if(menor > lista[i]):
            menor = lista[i]
            #print(f'Menor: {lista[i]}')
    return menor;

def linear5Menores(lista:list):
    menores = []
    copia = lista.copy() # permite manipula a lista sem alterar a lista original
    for i in range(0,5):
        menor = linearMenor(copia)
        #print(f'Menor Selecionado: {menor}')
        menores.append(menor)
        copia.remove(menor)
    return menores

def binariaMenor(lista:list):
    ordenada = lista.copy()
    ordenada.sort()
    return ordenada[0]

def binaria5Menores(lista:list):
    menores = []
    copia = lista.copy()
    for i in range(0,5):
        menor = binariaMenor(lista)
        #print(f'Menor Selecionado: {menor}')
        menores.append(menor)
        copia.remove(menor)
    return menores

def sort5Menores(lista:list):
    ordenada = lista.copy()
    ordenada.sort()
    return ordenada[0:5]

if __name__ == "__main__":
    lista = [78,45,33,78,90,12,30,11,28,40,8,1,5]
    # 1, 5, 8, 11, 12
    #  i * n - i
    print(linear5Menores(lista))
    print(binaria5Menores(lista))
    print(sort5Menores(lista))