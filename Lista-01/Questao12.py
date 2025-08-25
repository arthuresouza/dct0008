def contaDiv2(n):
    contaDivisores = 0;
    while (n >= 2):
        if(n % 2 == 0):
            contaDivisores += 1
        n = n/2        
    return contaDivisores


if  __name__ == "__main__":
    print(contaDiv2(8))