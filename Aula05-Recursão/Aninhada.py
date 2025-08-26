def h(n):
    if n == 0:
        return 0
    if n > 4:
        return n
    if n <= 4:
        return h(2+h(2*n))
    
def h_iterativo(n):
    """
    Para transformar uma recursão aninhada é necessário simula a pilha de chamadas recursivas
    """
    chamadasRecursivas = [(n, "chamada")]  # pilha com (valor, estado)
    
    while len(chamadasRecursivas) > 0:
        valor, estado = chamadasRecursivas.pop() # remove da pilha
        
        if estado == "retorno":
            if valor > 4:
                resultado = valor
            elif valor == 0:
                resultado = 0
            else:
                chamadasRecursivas.append((2 + resultado, "chamada"))
                continue
            return resultado
        
        else: 
            if valor == 0:
                resultado = 0
                return resultado
            elif valor > 4:
                resultado = valor
                return resultado
            else:
                chamadasRecursivas.append((valor, "retorno"))
                chamadasRecursivas.append((2*valor, "chamada"))


if __name__ == "__main__":
    print(f'h(1) = {h(1)}')
    print(f'h(2) = {h(2)}')
    print(f'h(3) = {h(3)}')