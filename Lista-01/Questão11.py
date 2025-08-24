
def ordenaListaArquivo(caminho):
    ordenados = [] # 1
    with open(caminho) as fil: # 1
        for linha in fil: # n
            #print(ordenados) 
            numero = int(linha.rstrip()); # n-1 * (2 + T(rstrip) = T(tamanho da string))
            if len(ordenados) > 0: # n-1 * 1
                i = 0 # n-1 * 1
                while(i < len(ordenados) and numero > ordenados[i]): # n-1 * Len(ordenados)  = n-1 * n
                    i += 1 # n-1 * n
                ordenados.insert(i,numero) # n-1 *n
            else:
                ordenados.insert(0,numero) # 1
    fil.close() # 1
    return ordenados # 1

if __name__ == "__main__":
    print(ordenaListaArquivo("/home/arthur/Documentos/Disciplinas/ED/Códigos-Exemplos/dct0008/Lista-01/numeros11.txt"))