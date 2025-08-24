"""
Códigos de Exemplos de Coleções em Python
Author:  Arthur Souza
"""

def printDicionarios():
   cores = {"vermelho": [255,0,0], "azul": [0,0,255], "verde": [0,255,0]}
   for cor in cores:
      print(f"{cor} : {cores[cor]}")
   cores.pop("vermelho")   
   print(cores)
   
   
   fusca = {"ano": 1985, "cor": "branca"}
   fusca.update({"motor": 1.6, "vagas": 4})
   print(fusca)
   fusca["ano"] = 1987
   fusca["preco"] = 30.000
   print(fusca)

   arthur = {"nome":"Arthur",  "idade": 40, "frutas": ["banana","maça"]}
   print(arthur["nome"])
   print(arthur.get('idade'))
   print(arthur.keys())
   print(arthur.values())
   

   josefina = {"nome":"Josefina", "idade": 85, "frutas": ["laranja","uva"]}
   print(arthur)
   print(josefina)

def printConjuntos():
   cores = {"verde","vermelho","azul"}
   coresRosa = set(("rosa","pink"))
   print(cores)
   print(coresRosa)

   numeros = {0,1,2,3,4,5,6,7,8,9,0}
   numeros.add(10)
   numeros.remove(0)
   print(numeros)

   impares = {1,3,5,7,9,11,13}
   primos = {2,3,5,7,11,13}
   imparesPrimos = impares.intersection(primos)
   paresPrimos = primos.difference(impares)
   imparesEprimos = impares.union(primos)
   print(imparesPrimos)
   print(paresPrimos)
   print(imparesEprimos)



def printTuplas():
   cores = ("verde","vermelho","azul")
   coresRosa = tuple(("rosa","pink"))
   print(cores)
   print(coresRosa)

   numeros = (0,1,2,3,4,5,6,7,8,9,0)
   print(numeros[2])
   print(numeros[1:2])
   print(4 in numeros)
   print(numeros.index(5))
   print(numeros.count(0))


def printListas():
   #remoção
   frutas = list(("Uva","Banana","laranja"))
   frutas.remove("Uva")
   frutas.pop(0)
   frutas.pop() #remove o último item
   frutas.clear() #limpa a lista

   #Consultando
   numeros = [0,1,2,3,4,5,6,7,8,9]
   print(numeros[2])
   print(numeros[1:2])
   print(numeros[-3:-1])
   print(4 in numeros)
   print(5 in numeros[0:3])
   print(numeros.index(5))


   #Criação
   vazia = []
   vazia2 = list()
   frutas = list(("Maça","Banana"))

   
   #Atualização
   nomes = ["Josefina","Astrogildo"]
   nomes.append("Maricota")
   nomes.insert(0,"Felisberto")
   nomes[1] = "Alcebiades"
   for item in nomes:
      print(item)

   for i in range(0,len(nomes)):
      print(nomes[i])



def printOperacoes():
   carros = ["fusca", "kombi", "gol", "fox", "amarok"]
   print("fusca" in carros)
   print("Voyage" in carros)
   print(len(carros))

   for c in carros:
      print(f"Carro: {c}")

   print(carros)

   linguagens = {"Java", "Python", "C", "C++"}
   print(len(linguagens))


def printColections():

   lista = [1,2.5,'3',4]
   tupla = (1,2.5,'3', 4)
   conjunto = {"Arthur", "Fabrício", "Flavius"}
   dicionario = {"nome": "Arthur", "sobrenome":"Souza"}
   texto = "Python é legal mas Java é melhor!!"
   
   print(f"Lista: {lista}")
   print(f"Tupla: {tupla}")
   print(f"Conjunto: {conjunto}")
   print(f"Dicionário: {dicionario}")
   print(f"String: {texto}")

   print("")

   for item in lista:
      print(f"Item de Lista: {item}")
  
   for item in lista:
      print(f"Item de Tupla: {item}")

   for item in conjunto:
      print(f"Item de Conjunto: {item}")

   for item in dicionario:
      print(f"Item de Dicionário: {item} : {dicionario[item]}")

   for item in texto:
      print(f"Item do Texto: {item}") 

def printStrings():
    print("Coleções em Python")
    print("A Lista é 'Linear'")
    print('A Tupla é "Linear"')

    multiLinha = """ Coleções em Python
    Lista
    Tupla
    """

    print(multiLinha)

    texto = "Python é show de bola !!"
    print(texto.index('é'))
    print(texto.replace("Python","Java"))

    for i in range(0,len(texto)):
       print(texto[i])

    numeros = "1234567"
    for num in numeros:
       print(num)
    
    print(numeros[0])
    print(numeros[:2])
    print(numeros[5:])
    print(numeros[-3:-4])
     

# Indentificando método para execução
if __name__ == "__main__":
   #printColections()
   #printStrings()   
   #printOperacoes()
   #printListas()
   #printTuplas()
   #printConjuntos()
   printDicionarios()