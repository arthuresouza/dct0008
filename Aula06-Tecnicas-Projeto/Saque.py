def saqueGuloso(valor, notas):
    saque = []
    for nota in notas:
        while valor >= nota:
            valor -= nota
            saque.append(nota)
    return saque

if __name__ == "__main__":
    #As notas devem estar ordenadas
    notas = [100, 50, 20, 10, 5, 2]
    valor = 64
    print("Saque Guloso:", saqueGuloso(valor, notas))
