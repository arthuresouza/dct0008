
def myRange(start, stop, step=1):
    sequencia = list() # 1
    i = 0 # 1
    if(step > 0): # 1
        while(i >= 0 and (start+step*i) < stop): # stop + 1 vezes
            sequencia.append(start+step*i) # stop vezes
            i += 1 # stop vezes
    elif(step < 0): # 0 ou 1
        while(i >= 0 and (start+step*i) > stop): # stop + 1 vezes 
            sequencia.append(start+step*i) # stop vezes
            i += 1 # stop vezes
    else: # 0 ou 1
        raise ValueError("Step zero não é permitido!")
    return tuple(sequencia)

if __name__ == "__main__":
    print(tuple(range(20,10,-1)))
    print(myRange(20,10,-1))



