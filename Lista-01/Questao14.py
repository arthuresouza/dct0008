import math

def a(n):
   if n == 1: return False
   for i in range(2,n):
       resto = n % i
       if resto == 0:
           return False
   return True

def b(n):
    if n == 1:
       return False
    if n == 2:
       return True
    if n % 2 == 0:
       return False
    i = 3
    while i <= math.sqrt(n):
       resto = n % i
       if resto == 0:
           return False
       else:
           i += 2    
    return True

if __name__ == "__main__":
   print(a(9))
   print(a(25))
   print(a(49))
   print(b(9))
   print(b(25))
   print(b(49))
   
