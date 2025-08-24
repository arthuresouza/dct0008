def removerDuplicados(lista):
    return set(lista) # 1

def removerDuplicadosFor(lista):
    unicos = set() # 1
    for item in lista: # n
        if item not in unicos: # n
            unicos.add(item) # 0 .. n
    return unicos # 1

if __name__ == "__main__":
    lista = ['maçã', 'banana', 'maçã', 'uva', 'laranja', 'uva']
    print(removerDuplicados(lista))
    print(removerDuplicadosFor(lista))