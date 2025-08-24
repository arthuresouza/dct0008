def lerItens():
    lista = list() # 1
    item = input("Digite o item ou '0' para finalizar: ") # 1
    while(item != "0"): # n + 1
        lista.append(item) # n
        item = input("Digite o item ou '0' para finalizar: ") # n
    print(f'Número de Itens inseridos: {len(lista)}') # 1
    print(f'Itens: {lista}') # 1

if __name__ == "__main__":
    lerItens()