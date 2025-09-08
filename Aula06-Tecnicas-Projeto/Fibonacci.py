def fibonacci(n):
    if n == 0: # 1
        return 0 # 1
    elif n == 1: # 1
        return 1 # 1
    else:        
        return fibonacci(n - 1) + fibonacci(n - 2) # 1,6^n * 3

def fibonacciPD(n):
    termos = [0,1]
    for i in range(2,n+1):
        termos.append(termos[i-1] + termos[i-2])
    return termos[n]



    
if __name__ == "__main__":
    for i in range(0,10):
        print(f'n: {i} =  {fibonacci(i)}')