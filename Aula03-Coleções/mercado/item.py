'''Módulo para representar um item do mercado, com descrição e preço.'''

def criarItem(descricao, preco, quantidade):
    ''' Função para criar um item do mercado. '''
    return {"descricao": descricao, "preco": preco, "quantidade": quantidade}

def imprimirItem(item):
    ''' Função para imprimir os detalhes de um item do mercado. '''
    print(f"Item: {item['descricao']}, Preço: R${item['preco']:.2f}")