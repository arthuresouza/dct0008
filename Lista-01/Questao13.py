import numpy

def soma(matriz1,matriz2):
    matrizResultado = numpy.empty((len(matriz1),len(matriz1)))
    for i in range(len(matriz1)):
       for j in range(len(matriz1)):
           #print(f'i: {i}, j: {j}, m1:{matriz1[i][j]}, m2: {matriz2[i][j]}')
           matrizResultado[i][j] = matriz1[i][j] + matriz2[i][j]
    return matrizResultado

def multiplicacao(matriz1,matriz2):
    matrizResultado = numpy.empty((len(matriz1),len(matriz1)))
    for i in range(len(matriz1)):
       for j in range(len(matriz2)):
           for k in range(len(matriz1)):
               matrizResultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return matrizResultado

def transpor(matriz1):
    for i in range(len(matriz1)):
        for j in range(i+1,len(matriz1)):
            copia = matriz1[i][j]
            matriz1[i][j] = matriz1[j][i]
            matriz1[j][i] = copia

if __name__ == "__main__":
    matriz1 = [[1,2,3],[1,2,3],[1,2,3]]
    matriz2 = [[3,4,5],[3,4,5],[3,4,5]]

    print(soma(matriz1,matriz2))
    print(multiplicacao(matriz1,matriz2))
    transpor(matriz1)
    print(matriz1)