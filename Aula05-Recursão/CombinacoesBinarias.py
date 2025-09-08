def combinacoesBinarias(n, combinacao=""):
    if len(combinacao) == n:
        print(combinacao)
        return    
    combinacoesBinarias(n, combinacao + "0")
    combinacoesBinarias(n, combinacao + "1")

"""
32 16 8 4 2 1

2 - 0-3 => 0 ate 2^n(-1)
3 - 4-7 => 2^(n-1) ate 2^n(-1)
4 - 8-15 => 2^(n-1)  

n=2 00, 01, 10, 11 
n=3 000, 001, 011, 010, 100, 110, 101, 111 
"""
def combinacoesBinariasIt(n):
    for i in range(0,2**(n)):
        binario=""       
        k=i
        #print(k)
        while(k>=1):
            binario = str(k%2) + binario
            k = k//2
        while(len(binario)<n):
            binario = "0" + binario
        print(binario)



if __name__ == "__main__":
    combinacoesBinariasIt(8)  
