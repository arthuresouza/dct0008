
def ordenaListaArquivoWhile(caminho):
    ordenados = [] # 1
    with open(caminho) as fil: # 1
        for linha in fil: # n
            #print(ordenados) 
            numero = int(linha.rstrip()); # n * (2 + T(rstrip) = T(tamanho da string))
            if len(ordenados) > 0: # n * 1
                i = 0 # n * 1
                while(i < len(ordenados) and numero > ordenados[i]): # n * Len(ordenados) - 1  = n * (n-1)
                    i += 1 # n * (n - 1)
                ordenados.insert(i,numero) # n                
            else:
                ordenados.insert(0,numero) # 1
    fil.close() # 1
    return ordenados # 1

def ordenaListaArquivoSort(caminho):
    ordenados = [] # 1
    with open(caminho) as fil: # 1
        for linha in fil: # n 
            numero = int(linha.rstrip()); # 1
            ordenados.append(numero) # 1
    fil.close() # 1
    return ordenados.sort() # n * log n

if __name__ == "__main__":
    print(ordenaListaArquivoWhile("/home/arthur/Documentos/Disciplinas/ED/Códigos-Exemplos/dct0008/Lista-01/numeros11.txt"))