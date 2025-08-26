def fatorial(n):
    if n == 0:
        print(f'Base: {n}! = 1')
        return 1
    else:
        print(f'Recursivo: {n}! = {n} * ({n-1})!')
        return n * fatorial(n-1)
    
def fatorialIterativo(n):
    fatorial = 1
    for i in range(1, n + 1):
        print(f"Multiplicando: {fatorial} * {i}")
        fatorial *= i
    return fatorial
    
if __name__ == "__main__":
    print(f'5! = {fatorial(5)}')
    print(f'5! = {fatorialIterativo(5)}')