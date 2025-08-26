def combinacoesBinarias(n, combinacao=""):
    if len(combinacao) == n:
        print(combinacao)
        return    
    combinacoesBinarias(n, combinacao + "0")
    combinacoesBinarias(n, combinacao + "1")