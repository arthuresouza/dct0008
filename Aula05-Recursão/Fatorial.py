def fatorial(n):
    if n == 0:
        print(f'Base: {n}! = 1')
        return 1
    else:
        print(f'Recursivo: {n}! = {n} * ({n-1})!')
        return n * fatorial(n-1)
    
if __name__ == "__main__":
    print(f'5! = {fatorial(5)}')