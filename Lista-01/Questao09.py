def divisores(n):
    divisores = {1,n} # 1
    for i in range(2, n//2 + 1): # n-1 / 2
        if n % i == 0: # n-1 / 2
            divisores.add(i) # 0 .. n-1 / 2
    return divisores # 1

if __name__ == "__main__":
    print(divisores(30))