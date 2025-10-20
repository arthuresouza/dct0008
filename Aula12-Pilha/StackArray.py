from Array import Array

class StackArray():

    def __init__(self):
        self.items = Array()
        self.topo = -1

    def __len__(self):
        return self.topo + 1

    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        """
        Ao usar o Iter de Array, o método retorna todos os elementos inclusive os None
        """
        pilhaTemp = list()
        for i in range(0,self.topo+1):
            pilhaTemp.append(self.items[i])
        return iter(pilhaTemp)
    
    def __contains__(self,item):
        for itemStack in self.items:
            if(itemStack == item):
                return True
        return False
        
    def __eq__(self, value):
        for itemStack in self.items:
            for itemValue in value:
                if(itemStack != itemValue):
                    return False
        return True
    
    def clear(self):
        self.items = Array()
        self.topo = -1

    def peek(self):
        if self.topo == -1:
            raise Exception("A pilha está vazia")
        return self.items[self.topo]
    def push(self, item):
        self.topo += 1
        self.items.insertAt(item,self.topo)
    
    def pop(self):
        if self.topo == -1:
            raise Exception("A pilha está vazia")
        item = self.items[self.topo]
        self.items[self.topo] = None
        self.topo -= 1
        return item
    
if __name__ == "__main__":
    pilha = StackArray()
    pilha.push(1)
    pilha.push(2)
    pilha.push(3)
    for i in pilha:
        print(pilha.pop())
    #for i in range(0,3):
    #    print(pilha.pop())
    