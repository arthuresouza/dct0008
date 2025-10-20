from LinkedList import LinkedList

class StackLinked2():

    def __init__(self):
        self.items = LinkedList()

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        pilhaTemp = list()
        for i in range(0,len(self.items)):
            pilhaTemp.append(self.items.getItemAt(i))
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
        self.items = LinkedList()

    def peek(self):
        if self.items.isEmpty():
            raise Exception("A pilha está vazia")
        return self.items.getItemAt(0)

    def push(self, item):
        self.items.insertAtFirst(item)
    
    def pop(self):
        if self.items.isEmpty():
            raise Exception("A pilha está vazia") 
        item = self.items.removeFirst()
        return item
    
if __name__ == "__main__":
    pilha = StackLinked2()
    pilha.push(1)
    pilha.push(2)
    pilha.push(3)
    for i in pilha:
        print(pilha.pop())
    #for i in range(0,3):
    #    print(pilha.pop())
    