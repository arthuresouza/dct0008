def imprimeMenores(n):
    if n == 1:
        print(1)
    else:        
        print(f'{n}')
        imprimeMenores(n-1)

def imprimeMenoresIt(n):
    for i in range(n,0,-1):
        print(i)
        

if __name__ == "__main__":
    imprimeMenores(5)
    imprimeMenoresIt(5)