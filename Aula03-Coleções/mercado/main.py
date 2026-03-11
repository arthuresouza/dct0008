'''Módulo principal do sistema de mercado.'''
from item import criarItem, imprimirItem

def abrirLista():
    ''' Função para abrir e manipular a lista de itens do mercado. '''
    listaItens = []
    while True:
        opcao = input("0 - Sair\n1 - Adicionar Item\n2 - Consultar Lista: ")
        match opcao:
            case "0":
                break
            case "1":
                nome = input("Descrição do item: ")
                preco = float(input("Preço do item: "))
                item = criarItem(nome, preco)
                listaItens.append(item)
            case "2":
                for item in listaItens:
                    imprimirItem(item)
    return listaItens

def finalizarLista(listaItens):
    ''' Função para finalizar a lista de compras, calculando o total. '''
    total = 0
    for item in listaItens:
        total += item['preco']
    print(f"Total da compra: R${total:.2f}")

def main():
    print("Bem-vindo ao Py Mercado!")
    
    opcao = -1
    while opcao != "0":
        opcao = input("0 - Sair\n1 - Abrir Lista\n2 - Finalizar Lista: ")
        listaItens = []
        match opcao:
            case "0":
                print("Encerrando programa.")
            case "1":
                listaItens = abrirLista()
            case "2":
                finalizarLista(listaItens)
            case _:
                continue

    
if __name__ == "__main__":
    main()
