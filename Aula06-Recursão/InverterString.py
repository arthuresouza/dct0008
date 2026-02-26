def inverter(texto,posicao=0):
    if posicao >= len(texto):
        return
    inverter(texto,posicao+1)
    print(texto[posicao])

def inverterIterativo(texto):
    for i in range(len(texto)-1,-1,-1):
       print(texto[i])
    

if __name__ == "__main__":
    inverter("12345")
    inverterIterativo("12345")