"""
Codigo para análise empirica da soma de inteiros positivos
"""
import time
import matplotlib.pyplot as plt

def somaInteirosWhile(maximo):
    soma = 0
    i=1
    while i <= (maximo+1):
        soma += i
        #print(f"Calculando While: {i} , total: {soma}")
        i += 1
    return soma

def somaInteirosPython(maximo):
    soma = sum(range(1,maximo+1))
    #print(f"Calculando Python Sum: , total: {soma}")
    return soma

def somaInteirosGauss(maximo):
    soma = maximo * ( maximo + 1) // 2
    #print(f"Calculando Gauss: , total: {soma}")
    return soma


def medirTempo(funcao, maximo):
    inicio = time.perf_counter()
    funcao(maximo)
    fim = time.perf_counter()
    return fim - inicio

def analiseEmpirica(numeros):
    resultados = {"While": [], "PythonSum": [], "Gauss": []}
    
    for n in numeros:
        resultados["While"].append(medirTempo(somaInteirosWhile, n))
        resultados["PythonSum"].append(medirTempo(somaInteirosPython, n))
        resultados["Gauss"].append(medirTempo(somaInteirosGauss, n))
    
    return resultados


def gerarGrafico(numeros, resultados):
    plt.figure(figsize=(10,6))
    plt.plot(numeros, resultados["While"], label="While", marker="o")
    plt.plot(numeros, resultados["PythonSum"], label="Python Sum ", marker="s")
    plt.plot(numeros, resultados["Gauss"], label="Gauss", marker="^")
    
    plt.xlabel("Quantidade de números",fontsize=18)
    plt.ylabel("Tempo de execução (sec)",fontsize=18)
    plt.title("Comparação de Algoritmos de Soma",fontsize=18)
    plt.legend()
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    maximo = 100000
    numeros = range(1,maximo)
    resultados = analiseEmpirica(numeros)
    gerarGrafico(numeros, resultados)
